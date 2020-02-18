# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Blueprint
import flask_restful as restful

from .routes import routes
#from .validators import security


#@security.scopes_loader
#def current_scopes():
    #return []

bp = Blueprint('v1', __name__, static_folder='static')
# 对蓝图bp注册api
api = restful.Api(bp, catch_all_404s=True)

# 将资源全部加入进api
for route in routes:
    api.add_resource(route.pop('resource'), *route.pop('urls'), **route)
