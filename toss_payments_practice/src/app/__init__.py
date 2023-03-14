from flask import Flask, url_for
from flask_cors import CORS

from app.controllers.view.general import bp as view

server=Flask(__name__)
server.register_blueprint(view,url_prefix='/')

CORS(server,resources={'*':{'origins':['*']}})