#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File：flask_api -> __init__.py
# @Author ：wangxintian
# @Date   ：2020/11/11 11:30 上午
# @Desc   ：

from flask import Flask
from flask_cors import *
from api import blueprint
from database import db, redis_store
from config.settings import default_setting


def create_app():
    app = Flask(__name__)
    configure_app(app)
    register_extensions(app)
    register_blueprints(app)
    return app


def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = default_setting.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = default_setting.SQLALCHEMY_COMMIT_ON_TEARDOWN
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = default_setting.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SWAGGER_UI_DOC_EXPANSION'] = default_setting.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config['RESTPLUS_VALIDATE'] = default_setting.RESTPLUS_VALIDATE
    app.config['RESTPLUS_MASK_SWAGGER'] = default_setting.RESTPLUS_MASK_SWAGGER
    app.config['ERROR_404_HELP'] = default_setting.RESTPLUS_ERROR_404_HELP
    app.config['REDIS_URL'] = default_setting.REDIS_URL
    app.config['FLASK_DEBUG'] = default_setting.FLASK_DEBUG
    # 输出原生sql语句，上线需要改成False
    app.config["SQLALCHEMY_ECHO"] = False


def register_extensions(app):
    CORS(app)
    db.init_app(app)
    redis_store.init_app(app)


def register_blueprints(app):
    blueprint.url_prefix = default_setting.FLASK_API_URL_PREFIX
    app.register_blueprint(blueprint)
