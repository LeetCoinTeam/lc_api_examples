import webapp2
import time
import json
import hashlib
import hmac
import urllib
import httplib
from handlers import BaseHandler
import logging
from config import *
from collections import OrderedDict

class DeactivatePlayerHandler(BaseHandler):
    def get(self):

        return self.render_html_response(
            'deactivate_player.html'
        )
    def post(self):
        """ send the list to the api server """
        platformid = self.request.get('platformid')
        rank = self.request.get('rank')
        satoshi_balance = self.request.get('satoshi_balance')
        
        logging.info("platformid: %s" %platformid)
        logging.info("rank: %s" %rank)
        logging.info("satoshi_balance: %s" %satoshi_balance)
        uri = "/api/deactivate_player"

        params = OrderedDict([
                  ("nonce", time.time()),
                  ("platformid", platformid),
                  #("rank", rank),
                  #("satoshi_balance", satoshi_balance)
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