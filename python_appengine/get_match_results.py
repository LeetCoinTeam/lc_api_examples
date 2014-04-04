import webapp2
import time
import json
import hashlib
import hmac
import urllib
import httplib
from config import *
from collections import OrderedDict

class GetMatchResultsHandler(webapp2.RequestHandler):
    def get(self):

        uri = "/api/get_match_results"
        
        params = OrderedDict([
                  ])
                          
        params = urllib.urlencode(params)


        headers = {"Content-type": "application/x-www-form-urlencoded"}
        if local_testing:
            conn = httplib.HTTPConnection(url)
        else:
            conn = httplib.HTTPSConnection(url)
        
        conn.request("POST", uri, params, headers)
        response = conn.getresponse()
                
        self.response.write(response.read())