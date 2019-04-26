# -*- coding:UTF-8 -*-
# extensions.py
# @author yanzhilong
# @description app第三方库的加载
# @created 20190426

import os
import logging
from datetime import datetime

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
    init_logger(app)
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
        app.logger.error(ex)
        app.mysql_pool = None
    finally:
        return


def init_logger(app):
    """
    初始化APP日志
    """

    def make_dir(make_dir_path):
        """
        文件夹创建
        """
        path = make_dir_path.strip()
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    app.logger.name = 'backup'
    # log配置，实现日志自动按日期生成日志文件
    log_dir_name = app.config['LOG_PATH'] if hasattr(
        app.config, 'LOG_PATH') else "logs"
    log_file_name = 'backup-' + \
        datetime.now().date().strftime('%Y-%m-%d') + '.log'
    log_file_folder = os.path.abspath(os.path.join(os.path.dirname(
        __file__), os.pardir, os.pardir)) + os.sep + log_dir_name
    make_dir(log_file_folder)
    print(log_file_folder)
    log_file_str = log_file_folder + os.sep + log_file_name
    file_handler = logging.FileHandler(log_file_str, encoding='UTF-8')
    file_handler.setLevel(logging.INFO)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    file_handler.setFormatter(logging_format)
    app.logger.addHandler(file_handler)
