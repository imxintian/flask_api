#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File：flask_api -> mysql_models.py
# @Author ：wangxintian
# @Date   ：2020/11/11 11:43 上午
# @Desc   ：
from database import db


class UserInfo(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    sex = db.Column(db.String(2))
    english = db.Column(db.Float)
    math = db.Column(db.Float)
    chinese = db.Column(db.Float)

    def __repr__(self):
        return '<UserInfo %r>' % self.id
