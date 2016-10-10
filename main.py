#-----------------------------------Details----------------------------------#
#                            Author: Raja sekhar                             #
#                        Creating a Blog Template                            #
#                        Template Engine: ninja2                             #
#                        Runtime: Python27                                   #
#----------------------------------------------------------------------------#


import webapp2
import jinja2
import os
from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                                  autoescape = True)

class Post(db.Model):
    title = db.StringProperty()
    content = db.TextProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template_file, **params):
        template = template_env.get_template(template_file)
        rendered_html = template.render(params)
        self.write(rendered_html)

class MainPage(Handler):
    def get(self):
        posts = db.GqlQuery('select * from Post')
        self.render('base.html', posts=posts)

class NewPost(Handler):
    def get(self):
        self.render('newPostForm.html')

    def post(self):
        title = self.request.get('postTitle')
        content = self.request.get('postContent')
        if title and content:
            newPost = Post()
            newPost.title = title
            newPost.content = content
            newPost.put()

class PostHandler(Handler):
    def get(self, postId):
        key = db.Key.from_path('Post',int(postId))
        post = db.get(key)
        print post
        self.render('post.html',post=post)




app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ('/newpost', NewPost),
                               (r'/post/(.+)', PostHandler)
                               ], debug = True)
