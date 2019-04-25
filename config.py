#
# config.py
# @author yanzhilong
# @description 
# @created Tue Nov 20 2018 13:05:07 GMT+0800 (中国标准时间)
# @last-modified Wed Nov 28 2018 12:55:03 GMT+0800 (中国标准时间)
#
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = True
    SERVER_HOST = '0.0.0.0'
    SERVER_PORT = 7003
    DB_USER = 'root'
    DB_PASSWORD = '123456'
    DB_HOST = 'db'
    DB_PORT = 3306
    DB_DATABASE = 'backup'
    DB_CHARSET = 'utf-8'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@db/backup'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
