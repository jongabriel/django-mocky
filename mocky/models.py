'''
Created on Aug 19, 2013

@author: jgabriel
'''
from django.db import models


OPTIONS = (
            ("application/json", "application/json"),
            ("text/plain", "text/plain"),
            )

'''
Representing a response to a Mocky call.
'''
class MockyResponse(models.Model):
    status_code = models.IntegerField(null=False, default=200)
    content_type = models.CharField(choices=OPTIONS, null=False, blank=False, max_length=1024)
    body = models.CharField(null=True, blank=True, max_length=8172)
    unique_code = models.CharField(max_length=256, null=False, blank=False)
    delay = models.IntegerField(null=False, default=0)
    encoding = models.CharField(max_length=64, null=False, default="UTF-8")
    #rest_verb = models.CharField(max_length=64) #the RESTful verb, if any; e.g., GET, POST, PUT
    #headers one-to-many
    
    