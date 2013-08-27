'''
Created on Aug 19, 2013

@author: jgabriel
'''

from django.core.urlresolvers import reverse
from django.forms.models import ModelForm
from django.http.response import HttpResponse
from django.shortcuts import render
from models import MockyResponse
import shortuuid


def create_url():
    unique_id = shortuuid.uuid()
    return unique_id


class MockyResponseForm(ModelForm):
    class Meta:
        model = MockyResponse
        fields = [ 'status_code', 'content_type', 'body', 'encoding']

        
def new_mock(request):
    get_mocky_url = None
    if request.method == 'POST':
        form = MockyResponseForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            inst = form.save(commit=False)
            unique = create_url()
            inst.unique_code = unique
            inst.save()
            
            #print "the rev is %s" %reverse('get_mocky', kwargs={'unique_code':unique})
            #print "the server name is %s" % request.get_host()
            get_mocky_url = "http://%s%s" %( request.get_host(), reverse('get_mocky', kwargs={'unique_code':unique} ) )
            print "the full url is %s" %get_mocky_url
            #return HttpResponse("Your mocky request URL is: %s" %get_mocky_url)
            form = MockyResponseForm() #create a new form
            #return render( request, 'create_service.html', { 'form': form, 'mocky_url': get_mocky_url } )
        else:
            #return errors in page/form
            return HttpResponse("error validating form %s" %form.errors)      
    else:
        form = MockyResponseForm()
    
    return render( request, 'create_service.html', { 'form': form, "mocky_url": get_mocky_url} )
        
def get_mocky(request, unique_code = None):
    #get the MockyResponse by the uuid
    if not unique_code:
        return new_mock(request)
    
    mocky_resp = MockyResponse.objects.get(unique_code=unique_code)
    print "the response is %s" % mocky_resp
    
    #create an http response from the created response
    c_type = "%s; charset=%s" %( mocky_resp.content_type , mocky_resp.encoding )
    resp = HttpResponse(content_type = c_type)
    resp.status_code = mocky_resp.status_code
    
    #encode the body here.
    resp.content = mocky_resp.body

    return resp
    
    
   
        