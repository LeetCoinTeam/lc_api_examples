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

## our player data structure
from player import Player

class SetMatchResultsHandler(BaseHandler):
    def get(self):
        
        return self.render_html_response(
            'match_results.html'
        )
        
    def post(self):
        """ send the list to the api server """
        
        map_title = self.request.POST.get('map_title')
        
        player_keys = self.request.get_all('player_key')
        logging.info(player_keys)
        
        player_names = self.request.get_all('player_name')
        logging.info(player_names)
        
        weapons = self.request.get_all('weapon')
        logging.info(weapons)
        
        kills = self.request.get_all('kills')
        logging.info(kills)
        
        deaths = self.request.get_all('deaths')
        logging.info(deaths)
        
        ranks = self.request.get_all('rank')
        logging.info(ranks)
        
        map_title = self.request.get_all('map_title')
        logging.info(map_title)

        playerlist = []
        
        for index, playerkey in enumerate(player_keys):
            player = Player(
                playerkey,
                int(kills[index]),
                int(deaths[index]),
                player_names[index],
                weapons[index],
                ranks[index]
            )
            # key, kills, deaths, name, weapon, rank
            
            playerlist.append(player.to_dict())
            
        player_json_list = json.dumps(playerlist)
            
        uri = "/api/put_match_results"
        
        params = OrderedDict([
                          ("map_title", map_title),
                          ("nonce", time.time()),
                          ("player_dict_list", player_json_list),
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