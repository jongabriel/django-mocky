from django.conf.urls import patterns, include, url
import mocky.views as views


urlpatterns = patterns('',
    url(r'^mocky_generate/$', views.new_mock, name='gen_mocky'),
    url(r'^get_mocky/(?P<unique_code>\w+)/$', views.get_mocky, name='get_mocky'),
        
)