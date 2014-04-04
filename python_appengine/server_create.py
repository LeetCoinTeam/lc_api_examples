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
from server import Server

class ServerCreateHandler(webapp2.RequestHandler):
    def get(self):

        uri = "/api/server_create"
        
        server = Server(
            "test server title",                            # title, 
            "102.168.0.1",                                  # hostAddress, 
            "10900",                                        # hostPort, 
            "192.168.0.1:10900",                            # hostConnectionLink, 
            "agxkZXZ-MTMzN2NvaW5yEQsSBEdhbWUYgICAgICAoAkM", # gameKey, 
            100,                                            # maxActivePlayers, 
            24,                                             # maxAuthorizedPlayers, 
            10000,                                          # minimumBTCHold,
            1000,                                           # incrementBTC, 
            0.01,                                           # serverRakeBTCPercentage, 
            None,                                           # serverAdminUserKey, 
            0.01,                                           # leetcoinRakePercentage, 
            False,                                          # allowNonAuthorizedPlayers, 
            "HIGH",                                         # stakesClass, 
            False,                                          # motdShowBanner, 
            "F00",                                          # motdBannerColor, 
            "test server",                                  # motdBannerText
        )
        
        server_json = json.dumps(server.to_small_dict())
        
        nonce = time.time()
        
        params = OrderedDict([
                  ("nonce", nonce),
                  ("server", server_json),
                  ])
                          
        params = urllib.urlencode(params)

        # Hash the params string to produce the Sign header value
        H = hmac.new(developer_shared_secret, digestmod=hashlib.sha512)
        H.update(params)
        sign = H.hexdigest()
        
        logging.info("Sign: %s" %sign)
        logging.info("nonce: %s" %nonce)
        logging.info("developer_api_key: %s" %developer_api_key)
        

        headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Key":developer_api_key,
                           "Sign":sign}
        if local_testing:
            conn = httplib.HTTPConnection(url)
        else:
            conn = httplib.HTTPSConnection(url)
        
        conn.request("POST", uri, params, headers)
        response = conn.getresponse()
                
        self.response.write(response.read())