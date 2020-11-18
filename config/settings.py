#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File：flask_api -> settings.py
# @Author ：wangxintian
# @Date   ：2020/11/11 11:33 上午
# @Desc   ：
# -*- coding: UTF-8 -*-
FLASK_ENV = 'dev'  # FLASK deployment env dev/prod


class DefaultSetting(object):
    """Default configuration."""
    FLASK_API_URL_PREFIX = '/flask/api'  # URL Prefix
    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'mysql://root:wxtzuo0218!@localhost:3306/employees?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SQLALCHEMY_BINDS = {
        'mysql_skyeye_v4': 'mysql://yxt:YXTsip.fhgj2910@10.10.49.165:3306/skyeyev4?charset=utf8'
    }

    # Redis settings
    REDIS_URL = 'redis://:YXTsip.fhgj2910@10.10.181.19/4'
    REDIS_KEY_PREFIX = "dev:skyeyeapi_v4:"
    REDIS_KEY_PREFIX_JOB = "dev:skyeyeapi_v4.job:"
    # REDIS_KEY_PREFIX_WXT_JOB = "devint:skyeye_v4_wxt.job:"
    REDIS_DEFAULT_TIMEOUT = 24 * 60 * 60

    HMAC_KEY = 'd08c33217cc38cdbc287a6eaea2b751e24150eaf011fad87e419c7f73becfceb'


class DevSetting(DefaultSetting):
    """Development configuration."""
    FLASK_DEBUG = True  # Do not use debug mode in production
    FLASK_LOGGER = 'debugLogger'


class ProdSetting(DefaultSetting):
    """Production configuration."""
    FLASK_DEBUG = False  # Do not use debug mode in production
    FLASK_LOGGER = 'errorLogger'  # Logger


default_setting = DevSetting
if FLASK_ENV == 'prod':
    default_setting = ProdSetting

