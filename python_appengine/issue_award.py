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

## Our award data structure
from award import Award

class IssueAwardHandler(BaseHandler):
    def get(self):

        return self.render_html_response(
            'issue_award.html'
        )
    def post(self):
        """ send the list to the api server """
        player_key = self.request.get('player_key')
        logging.info(player_key)
        
        player_name = self.request.get('player_name')
        logging.info(player_name)
        
        award_amount = self.request.get('award_amount')
        logging.info(award_amount)
        
        award_title = self.request.get('award_title')
        logging.info(award_title)
        
        award = Award(
            player_key,
            player_name,
            int(award_amount),
            award_title
        )
        
        award_json = json.dumps(award.to_dict())
            
        uri = "/api/issue_award"
        
        
        params = OrderedDict([
                ("award", award_json),
                ("nonce", time.time()),
                  ])
                          
        params = urllib.urlencode(params)
        
        logging.info(params)

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