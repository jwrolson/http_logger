import os
import json
import logging
import logging.handlers
import configparser
import falcon
import LoggerAPI

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = '{0}/poster.cfg'.format(CURRENT_DIR)

CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)

#app = falcon.API(middleware=[LoggerAPI.RequireJSON(),LoggerAPI.JSONTranslator()])
app = falcon.API(middleware=[LoggerAPI.JSONTranslator()])

sections = CONFIG.sections()
for section in sections:
    endpoint = section
    log_name = CONFIG.get(section, 'log_name')
    json_post = LoggerAPI.PostEvent(log_name)
    app.add_route(endpoint, json_post)
