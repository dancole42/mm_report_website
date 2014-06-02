from google.appengine.api import users
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        auth = ['dancole42@gmail.com',
                'jordana20@gmail.com']
        user = users.get_current_user()
        #if user:
        #    greeting = ('Welcome, %s - %s! (<a href="%s">sign out</a>)' %
        #                (user.nickname(), user.email(), users.create_logout_url('/')))
        if user:
            if user.email() in auth:   
                greeting = ('Welcome, %s - %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), user.email(), users.create_logout_url('/')))
            else:
                greeting = ('<a href="%s">You are not authorized to access this reportt</a>.' %
                        users.create_login_url('/'))
        else:
            greeting = ('<a href="%s">You must sign in to access this report</a>.' %
                        users.create_login_url('/'))

        self.response.out.write('<html><body>%s</body></html>' % greeting)
        
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)