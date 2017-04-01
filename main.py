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
import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASS_RE.match(password)

def valid_email(email):
    return MAIL_RE.match(email)

def build_page(username='', email='', name_error='', pass_error='', verify_error='', mail_error=''):

    head = "<style> .error {color: red;}</style>"
    header = "<h1>" + "User Signup Form" + "</h1>"

    name_label = "<td><label>Username</label></td>"
    name_span = "<td><span class='error'>{0}</span></td>".format(name_error)
    name_area = "<td><input type='text' name='username' value='{0}' required>".format(username) + "</input></td>"
    pass_label = "<td><label>Password</label></td>"
    pass_span = "<td><span class='error'>{0}</span></td>".format(pass_error)
    pass_area = "<td><input type='password' name='password' required/></td>"
    verify_label = "<td><label>Verify Password</label></td>"
    verify_span = "<td><span class='error'>{0}</span></td>".format(verify_error)
    verify_area = "<td><input type='password' name='verify' required/></td>"
    email_label = "<td><label>Email (Optional)</label></td>"
    email_span = "<td><span class='error'>{0}</span></td>".format(mail_error)
    email_area = "<td><input type='email' name='email' value ='{0}'>".format(email) + "</input></td>"
    submit = "<td><input type='submit'/></td>"

    form = ("<form method='post'>" + "<table>" +
        "<tr>" + name_label + name_area + name_span + "</tr>" +
        "<tr>" + pass_label + pass_area + pass_span + "</tr>" +
        "<tr>" + verify_label + verify_area + verify_span + "</tr>" +
        "<tr>" + email_label + email_area + email_span +  "</tr>" +
        "<tr>" + submit + "</tr>" +
        "</table>" +
        "</form>")

    return head + header + form


class MainHandler(webapp2.RequestHandler):

    def get(self):
        content = build_page('')
        self.response.write(content)


    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        name_check = valid_username(username)
        pass_check = valid_password(password)
        mail_check = valid_email(email)


        if not mail_check:
            if email == '':
                mail_check = True

        if not name_check:
            name_error = "Please enter a valid username"
        else:
            name_error = ''

        if not pass_check:
            pass_error = "Please enter a valid password"
        else:
            pass_error = ''

        if password != verify:
            verify_error = "Passwords do not match"
            verified = False
        else:
            verify_error = ''
            verified = True

        if not mail_check:
            mail_error = "Please enter a valid email address"
        else:
            mail_error = ''


        if name_check and pass_check and mail_check and verified:
            self.redirect("/welcome/?username="+username)
        else:
            content = build_page(username, email, name_error, pass_error, verify_error, mail_error)
            self.response.write(content)


class WelcomeHandler(webapp2.RequestHandler):

    def get(self):
        username = self.request.get('username')
        content = "<h1>{0}</h1>".format("Welcome " + username + "!")
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome/', WelcomeHandler)
], debug=True)
