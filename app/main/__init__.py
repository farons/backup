# -*- coding:UTF-8 -*-
# __init__.py
# @author yanzhilong
# @description 这里配置所有要注册的模块,模块下的所有文件都是分模块的功能
# @created 20181020

from .views import main
from .users import users


BluePrint = [
    (main, '/'),
    (users, '/users')
]


def config_blueprint(app):
    """
    app注册蓝图方法
    """
    for blueprint, prefix in BluePrint:
        app.register_blueprint(blueprint, url_prefix=prefix)
