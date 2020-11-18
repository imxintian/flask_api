#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File：flask_api -> __init__.py.py
# @Author ：wangxintian
# @Date   ：2020/11/12 3:57 下午
# @Desc   ：
import os
import logging.config
from config.settings import *

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../config/logging.conf')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

if FLASK_ENV == 'prod':
    log = logging.getLogger('errorLogger')
else:
    log = logging.getLogger('debugLogger')
