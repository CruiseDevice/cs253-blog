import os


import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a,**kw)

    def render_str(self,template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self,template,**kw):
        self.write(self.render_str(template,**kw))


class MainPage(Handler):

    def get(self):
        self.render('blog.html')

class NewPost(Handler):

    def get(self):
        self.render('newpost.html')

    def post(self):
        title = self.request.get("title")
        post = self.request.get("post")

        if title and post:
            self.render("thanks")
        else:
            error = "we need both a title and some blog post"
            self.render("newpost.html",error = error)

app = webapp2.WSGIApplication([('/',MainPage),
                                ('/newpost',NewPost)],
                                debug=True)
