#
# config.py
# @author yanzhilong
# @description 
# @created Tue Nov 20 2018 13:05:07 GMT+0800 (中国标准时间)
# @last-modified Wed Nov 28 2018 12:55:03 GMT+0800 (中国标准时间)
#
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  # 设置系统环境变量
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    

class DevelopmentConfig(Config):    # 开发环境
    ENV = 'development'
    DEBUG = True
    SERVER_NAME = '0.0.0.0:7004'


class TestingConfig(Config):    # 测试环境
    ENV = 'testing'
    DEBUG = True
    TESTING = True
    SERVER_NAME = '0.0.0.0:7003'
    DB_USER = 'root'
    DB_PASSWORD = '123456'
    DB_HOST = '148.70.37.64'
    DB_PORT = 7013
    DB_DATABASE = 'backup'
    DB_CHARSET = 'utf-8'

class ProductionConfig(Config):  # 生产环境
    ENV = 'production'
    DEBUG = False
    SERVER_NAME = '0.0.0.0:7001'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


