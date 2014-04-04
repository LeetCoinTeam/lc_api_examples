import webapp2
import time
import json
import hashlib
import hmac
import urllib
import httplib
import logging
from collections import OrderedDict
from config import *

class ServerInfoHandler(webapp2.RequestHandler):
    def get(self):

        uri = "/api/get_server_info"
        
        params = OrderedDict([
                  ("nonce", time.time()),
                  ])
                          
        params = urllib.urlencode(params)

        # Hash the params string to produce the Sign header value
        H = hmac.new(shared_secret, digestmod=hashlib.sha512)
        H.update(params)
        sign = H.hexdigest()

        headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Key":api_key,
                           "Sign":sign}
        if local_testing:
            conn = httplib.HTTPConnection(url)
        else:
            conn = httplib.HTTPSConnection(url)
        
        conn.request("POST", uri, params, headers)
        response = conn.getresponse()
                
        self.response.write(response.read())