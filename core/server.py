import tornado.ioloop
import tornado.web

class IndexHander(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")
