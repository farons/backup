#
# manage.py
# @author yanzhilong
# @description 启动app
# @created Sat Nov 24 2018 10:59:08 GMT+0800 (中国标准时间)
# @last-modified Wed Nov 28 2018 12:49:45 GMT+0800 (中国标准时间)
#


import os

from flask_script import Manager, Server
from app import create_app

# TODO: 完善启动模块,即是在其中加入命令运行模块
# TODO: api文档生产
# TODO: 完善环境配置
# TODO: 添加数据库相关配置
# TODO: 添加登录模块
# TODO: 添加logging模块支持

app = create_app("testing")
manager = Manager(app)

@manager.option('-n','--name', dest='name', help='运行用户名称', default='test')
@manager.option('-u','--url', dest='url', help='用户地址', default='www.baidu.com')
def cmd(name,url):
    print(name,url)

if __name__ == '__main__':
    manager.run()