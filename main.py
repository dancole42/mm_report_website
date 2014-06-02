from google.appengine.api import users
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        auth = ['dancole42@gmail.com',
                'jordana20@gmail.com']
        styles = '<head><style><link href="/stylesheets/stylesheet.css" type="text/css" rel="stylesheet" /></style></head>'
        user = users.get_current_user()
        #if user:
        #    greeting = ('Welcome, %s - %s! (<a href="%s">sign out</a>)' %
        #                (user.nickname(), user.email(), users.create_logout_url('/')))
        if user:
            if user.email() in auth:   
                greeting = ('Welcome, %s - %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), user.email(), users.create_logout_url('/')))
            else:
                greeting = ('<a href="%s">You are not authorized to access this report</a>.' %
                        users.create_login_url('/'))
        else:
            greeting = ('<a href="%s">You must sign in to access this report</a>.' %
                        users.create_login_url('/'))

        self.response.out.write('<html>%s<body><div class="auth">%s</div></body></html>' % (styles, greeting))
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)