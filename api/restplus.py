import traceback

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound
# from log import log
from log import log

api = Api(version='1', title='flask_api_example',
          description='flask_api_example')

fun_dict = {
    'resp_204': api.response(
        204,
        'successfully updated.'),
    'resp_401': api.response(
        401,
        'token auth fail.'),
    'resp_403': api.response(
        403,
        'access forbidden.'),
    'resp_404': api.response(
        404,
        'no result found or update object not exist'),
    'expect': api.expect,
    'marshal1': api.marshal_with,
    'marshal2': api.marshal_list_with}


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    if not globals()['FLASK_DEBUG']:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404


def decorator_compose(*funs):
    def decorator(f):
        for fun in reversed(funs):
            f = fun(f)
        return f
    return decorator
