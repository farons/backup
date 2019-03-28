from config import config
from flask import Flask

app = Flask(__name__)

def create_app(app, config_name=None):
    # 加载默认配置
    if config_name:
        app.config.from_object(config[config_name])
    # 注册蓝图    
    from .main import view_modules as buleprint_modules 
    for key in buleprint_modules:
        app.register_blueprint(key,url_prefix=buleprint_modules[key])
    
    # 创建数据库连接
   # try:
   #     if not hasattr(g,'POOL'):
   #         g.POOL = PooleDB(creator=pymysql,maxconnection=6,mincached=5,maxcached=3,maxshared=3,
   #                 blocking=True,maxusage=None,setsessioin=[],ping=0,host=app['DB_HOST'],port=app['DB_PORT'],
   #                 user=app['DB_USER'],password=app['DB_PASSWORD'],database=app['DB_DATABASE'],charset=app['DB_CHARSET'])
   # except Exception as ex:
   #     print(ex)
    return app
