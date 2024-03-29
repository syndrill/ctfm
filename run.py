from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app
import os

print("running on http://0.0.0.0:{}/".format(5000 if os.getenv("PORT") is None else int(os.getenv("PORT"))))

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000 if os.getenv("PORT") is None else int(os.getenv("PORT")),'0.0.0.0')
IOLoop.instance().start()
