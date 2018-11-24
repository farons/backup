#
# manage.py
# @author yanzhilong
# @description 启动app
# @created Sat Nov 24 2018 10:59:08 GMT+0800 (中国标准时间)
# @last-modified Sat Nov 24 2018 11:36:36 GMT+0800 (中国标准时间)
#


import os

from app import create_app


app = create_app("testing")

if __name__ == '__main__':
    app.run()