# -*- coding: UTF-8 -*-
import tornado.ioloop
import tornado.web

from handlers import config
from handlers import database
from handlers import fileserver
from lender import application
# import socket
# g_server_ip = socket.gethostbyname(socket.gethostname())
import argparse

def get_args_parser():
    parser = argparse.ArgumentParser(description="lender command line interface.")
    parser.add_argument("-c", "--config", default='config.ini', help="配置文件路径")
    parser.add_argument("-p", "--port", default=80, type=int, help="配置文件路径")
    return parser.parse_args()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def Run():
    args = get_args_parser()
    print(args)

    config.Parse(args.config)
    # print(config.CONFIG)

    handler = []
    handler.extend(database.Handle(config.Get_database()))
    handler.extend(fileserver.Handle(config.Get_fileserver()))
    handler.extend(fileserver.Handle(config.Get_index()))
    application.Serving(int(args.port), handler)
    
    
if __name__ == "__main__":
    Run()
