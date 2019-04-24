# -*- coding:UTF-8 -*-
# manage.py
# @author yanzhilong
# @description 启动app
# @created Sat Nov 24 2018 10:59:08 GMT+0800 (中国标准时间)
# @last-modified Wed Nov 28 2018 12:49:45 GMT+0800 (中国标准时间)
#
import sys

from app import app

if __name__ == '__main__':
    app.run(host=app.config['SERVER_HOST'],port=app.config['SERVER_PORT'],debug=app.config['DEBUG'])
