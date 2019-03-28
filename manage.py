# -*- coding:UTF-8 -*-
# manage.py
# @author yanzhilong
# @description 启动app
# @created Sat Nov 24 2018 10:59:08 GMT+0800 (中国标准时间)
# @last-modified Wed Nov 28 2018 12:49:45 GMT+0800 (中国标准时间)
#


import sys
import argparse

from flask import Flask

from app import create_app


# TODO: api文档生产
# TODO: 添加数据库相关配置
# TODO: 添加登录模块
# TODO: 添加logging模块支持


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="your script description")
    parser.add_argument('-c', '--config', default='testing', help='config name',dest='config_name')
    args = parser.parse_args(sys.argv[1:])
    
    backup = create_app(args.config_name)
    backup.run()
