from django.test.client import Client
from django.test.testcases import LiveServerTestCase


class MockyTest(LiveServerTestCase):
    
    def setUp(self):
        self.the_client = Client()
         
                   
    
    def test_simple_text(self):
        response = self.the_client.post( '/mocky_generate/', {'status_code': '200', 'content_type': 'text/plain', 
                                                             "body": "Plain text returned!", "encoding": "utf-8"} )
        
        print "test response is %s" %response