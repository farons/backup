from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

from DBUtils.PooledDB import PooledDB
import pymysql

# 扩展库的实例化
db = SQLAlchemy()
migrate = Migrate(db=db)
login_manager = LoginManager()
mail = Mail()


def config_extentions(app):
    """
    统一进行app的初始化操作
    """
    db.init_app(app)
    migrate.init_app(app=app)
    login_manager.init_app(app=app)
    mail.init_app(app)
    init_mysql(app)


def init_mysql(app):
    """
    初始化mysql连接池
    """
    try:
        app.mysql_pool = PooledDB(creator=pymysql,
                                  maxconnections=6,
                                  mincached=5,
                                  maxcached=3,
                                  maxshared=3,
                                  blocking=True,
                                  maxusage=None,
                                  setsession=[],
                                  ping=0,
                                  host=app.config['DB_HOST'],
                                  port=app.config['DB_PORT'],
                                  user=app.config['DB_USER'],
                                  password=app.config['DB_PASSWORD'],
                                  database=app.config['DB_DATABASE'])
    except Exception as ex:
        print(ex)
        app.mysql_pool = None
    finally:
        return
