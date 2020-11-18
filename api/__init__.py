#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File：flask_api -> __init__.py.py
# @Author ：wangxintian
# @Date   ：2020/11/11 10:41 上午
# @Desc   ：
from flask import Blueprint
from config.settings import *
from api.restplus import api

from api.test import ns as test_namespace


blueprint = Blueprint('api', __name__, url_prefix=DefaultSetting.FLASK_API_URL_PREFIX)
api.init_app(blueprint)

api.add_namespace(test_namespace)


