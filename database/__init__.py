#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File：flask_api -> __init__.py.py
# @Author ：wangxintian
# @Date   ：2020/11/11 11:32 上午
# @Desc   ：
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from config.settings import default_setting

db = SQLAlchemy()
session = db.session

redis_store = FlaskRedis()
