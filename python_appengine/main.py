#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import time
import json
import hashlib
import hmac
import urllib
import httplib
from auth_test import AuthTestHandler
from server_info import ServerInfoHandler
from match_results import SetMatchResultsHandler
from activate_player import ActivatePlayerHandler
from deactivate_player import DeactivatePlayerHandler
from get_match_results import GetMatchResultsHandler
from issue_award import IssueAwardHandler
from server_create import ServerCreateHandler

class MainHandler(webapp2.RequestHandler):
    def get(self):

        nav_page = """
        <html>
        <body>
        <h2>Developer Key</h2>
        <a href="/server_create">Server Create</a><br>
        <h2>Server Key</h2>
        <a href="/auth_test">Authentication Test </a><br>
        <a href="/server_info"> Server Info Call </a><br>
        <a href="/activate_player">Activate Player</a><br>
        <a href="/deactivate_player">Deactivate Player</a><br>
        <a href="/match_results">Set Match results</a><br>
        <a href="/get_match_results">Get Match results</a><br>
        <a href="/issue_award">Issue Award</a><br>
        </body>
        </html>
        """
                
        self.response.write(nav_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/auth_test', AuthTestHandler),
    ('/server_info', ServerInfoHandler),
    ('/activate_player', ActivatePlayerHandler),
    ('/deactivate_player', DeactivatePlayerHandler),
    ('/match_results', SetMatchResultsHandler),
    ('/get_match_results', GetMatchResultsHandler),
    ('/issue_award', IssueAwardHandler),
    ('/server_create', ServerCreateHandler)
], debug=True)
