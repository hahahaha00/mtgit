import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options

settings={'debug':True}
define('port',default=9999,help='run on the given port',type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')

    def post(self):
        pass

class InputHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/input.html')

    def post(self):
        pass

class SearchHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/search.html')

    def post(self):
        pass

class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/manager.html')

    def post(self):
        pass

def MainProcess():
    tornado.options.parse_command_line()
    application = tornado.web.Application(
            [(r'/',MainHandler),
             (r'/input',InputHandler),
             (r'/search',SearchHandler),
             (r'/manager',ManagerHandler),],
            **settings
        )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__=='__main__':
    MainProcess()
