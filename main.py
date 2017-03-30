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

def build_page(username='', password='', confirm='', email=''):
    head = "<h2>" + "User Signup Form" + "</h2>"

    name_label = "<label>Username</label>"
    name_area = "<input type='text' name='username'>" + username + "</input>"
    pass_label = "<label>Password</label>"
    pass_area = "<input type='password' name='password'>" + password + "</input>"
    confirm_label = "<label>Confirm Password</label>"
    confirm_area = "<input type='password' name='confirm'>" + confirm + "</input>"
    email_label = "<label>Email (Optional)</label>"
    email_area = "<input type='text' name='email'>" + email + "</input>"
    submit = "<input type='submit'/>"

    form = ("<form method='post'>" + "<table>" +
        "<tr>" + "<td>" + name_label + "</td>" + "<td>" + name_area + "</td>" + "</tr>" +
        "<tr>" + "<td>" + pass_label + "</td>" + "<td>" + pass_area + "</td>" + "</tr>" +
        "<tr>" + "<td>" + confirm_label + "</td>" + "<td>" + confirm_area + "</td>" + "</tr>" +
        "<tr>" + "<td>" + email_label + "</td>" + "<td>" + email_area + "</td>" + "</tr>" +
        "<tr>" + "<td>" + submit + "</td>" + "</tr>" +
        "</table>" +
        "</form>")

    return head + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page('')

        self.response.write(content)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        confirm = self.request.get("confirm")
        email = self.request.get("email")

        content = build_page(username, password, confirm, email)

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
