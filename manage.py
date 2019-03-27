# -*- coding:UTF-8 -*-
# manage.py
# @author yanzhilong
# @description 启动app
# @created Sat Nov 24 2018 10:59:08 GMT+0800 (中国标准时间)
# @last-modified Wed Nov 28 2018 12:49:45 GMT+0800 (中国标准时间)
#


import os

from flask_script import Manager, Server

from app import create_app
from config import config
# TODO: 完善启动模块,即是在其中加入命令运行模块
# TODO: api文档生产
# TODO: 完善环境配置
# TODO: 添加数据库相关配置
# TODO: 添加登录模块
# TODO: 添加logging模块支持

app = create_app()
manager = Manager(app)

@manager.option('-c', '--config', dest='config_name', help='config file', default='testing')
# 初始化配置
def init_config(config_name='testing'):
    """
    根据输入参数初始化配置文件
    """
    try:
        app.config.from_object(config[config_name])
        config[config_name].init_app(app)
    except:
        pass


if __name__ == '__main__':
    manager.run()
