import pymysql
from DBUtils.PooledDB import PooledDB

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


app = Flask(__name__, instance_relative_config=True)
# 加载默认配置
app.config.from_object(Config)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.POOL = PooledDB(creator=pymysql,
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

from app import models
from .main import view_modules as buleprint_modules
for key in buleprint_modules:
    app.register_blueprint(key,url_prefix=buleprint_modules[key])
