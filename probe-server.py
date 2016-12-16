#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html", list_info=[11, 22, 33])

application = tornado.web.Application([
    (r"/index", MainHandler),
])


if __name__ == "__main__":
    application.listen(6664)
    tornado.ioloop.IOLoop.instance().start()
