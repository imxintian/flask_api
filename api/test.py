#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project -> File：flask_api -> test.py
# @Author ：wangxintian
# @Date   ：2020/11/11 10:43 上午
# @Desc   ：
from flask import request
from flask_restplus import Namespace, Resource, fields

from api.restplus import fun_dict, decorator_compose
from database import session
from database.mysql_models import UserInfo

ns = Namespace('test', description='user_increase related operations')

score_param = ns.model('score param', {
    'name': fields.String(required=True, description='姓名')
})

id_param = ns.model('id param', {
    'id': fields.String(required=True, description='学号')
})


@ns.doc('根据用户id添加返回成绩')
@ns.route('/idx')
class Accumulate(Resource):
    @ns.expect(id_param)
    @decorator_compose(fun_dict['resp_401'], fun_dict['resp_404'])
    def put(self):
        id = request.get_json().get('id', '11')
        f = session.execute(f"""select * from user where id ={id}""").fetchall()
        if f:
            return {'message': "这条数据已存在"}, 200
        else:
            user = UserInfo(id=int(id), name='leo', english=99.0, chinese=86.0, math=90.0, sex=0)
            print(user)
            session.add(user)
            session.commit()
        return 200


@ns.doc('输入根据用户名返回成绩')
@ns.route('/score')
class Accumulate(Resource):
    @ns.expect(id_param)
    @decorator_compose(fun_dict['resp_401'], fun_dict['resp_404'])
    def post(self):
        name = request.get_json().get('name', 'neo')
        # 方法1, 使用orm
        # score = session.query(UserInfo.id, UserInfo.chinese,  UserInfo.english).filter(UserInfo.name == name).all()
        # 方法2，使用sql
        score = session.execute(f"""select id,chinese,english from user where name ='{name}'""").fetchall()
        result = {
            '姓名': name,
            'id': score[0][0],
            '成绩': {
                '语文': score[0][1],
                '数学': score[0][2]
            }
        }
        return result
        pass


@ns.route('/id')
class Accumulate(Resource):
    @ns.expect(id_param)
    @decorator_compose(fun_dict['resp_401'], fun_dict['resp_404'])
    def delete(self):
        id = int(request.get_json().get('id', '11'))
        f = session.execute(f"""select * from user where id ={id}""").fetchall()
        if f:
            session.execute(f"""delete from user where id ={id}""")
            session.commit()
        else:
            return {'message': "这条数据不存在"}, 200
        return 200

    @decorator_compose(fun_dict['resp_401'], fun_dict['resp_404'])
    def get(self):
        id = int(request.args.get('id', '12'))
        f = session.execute(f"""select * from user where id ={id}""").fetchall()
        if f:

            return {'id': f[0][0],
                    'name': f[0][1],
                    'sex': f[0][2],
                    'english': f[0][3],
                    'math': f[0][4],
                    'chinese': f[0][5]}

        else:
            return {'message': "这条数据不存在"}, 200
