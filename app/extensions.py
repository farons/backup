# -*- coding:UTF-8 -*-
# extensions.py
# @author yanzhilong
# @description app第三方库的加载
# @created 20190426

import os
import logging
from logging.handlers import MemoryHandler
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

from DBUtils.PooledDB import PooledDB
import pymysql

# import sys
# import codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
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
    init_mysql(app, 3)


def init_mysql(app, restart_times=3):
    """
    初始化mysql连接池
    """
    while restart_times > 0:
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
            restart_times = 0
        except Exception as ex:
            app.logger.error(ex)
            app.mysql_pool = None
            restart_times -= 1
            continue


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
    # log配置,实现日志自动按日期生成日志文件
    log_dir_name = app.config['LOG_PATH'] if hasattr(
        app.config, 'LOG_PATH') else "logs"
    base_path = os.path.realpath('.')
    log_file_name = 'backup-' + \
        datetime.now().date().strftime('%Y-%m-%d') + '.log'
    log_file_folder = base_path + os.sep + log_dir_name
    make_dir(log_file_folder)
    log_file_str = log_file_folder + os.sep + log_file_name
    file_handler = logging.FileHandler(
        log_file_str, encoding='UTF-8')
    file_handler.setLevel(logging.INFO)
    logging_format = logging.Formatter(
        '%(name)s - %(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    file_handler.setFormatter(logging_format)
    # 更改默认的日志显示格式
    app.logger.handlers[0].setFormatter(logging_format)
    app.logger.addHandler(file_handler)

    # log配置,优化后的邮件通知
    if ('LOG_EMAIL_HOST' in app.config.keys()) and (app.config['TESTING'] is False):
        memory_handler = OptmizedMemoryHandler(app.config['LOG_EMAIL_MAX'], "backup后台程序", app.config['LOG_EMAIL_HOST'],
                                               app.config['LOG_EMAIL_PORT'], app.config['LOG_EMAIL_USER'],
                                               app.config['LOG_EMAIL_PASSWD'],
                                               app.config['LOG_EMAIL_FROM'], app.config['LOG_EMAIL_TO'])
        memory_handler.setLevel(logging.ERROR)
        memory_handler.setFormatter(logging.Formatter(logging_format))
        app.logger.addHandler(memory_handler)


class OptmizedMemoryHandler(MemoryHandler):
    """
    优化logger的MermoryHandler,解决同样的问题多次邮件发送的问题
    """

    def __init__(self, capacity, mail_subject, mail_host, mail_port, mail_from_user, mail_from_passwd, mail_from, mail_to):
        """ 
        capacity: flush memory
        mail_subject: 标题
        mail_host: 邮箱服务host
        mail_from: 发送邮箱地址
        mail_to: 列表格式
        """
        logging.handlers.MemoryHandler.__init__(self, capacity, flushLevel=logging.ERROR,
                                                target=None)
        self.mail_subject = mail_subject
        self.mail_host = mail_host
        self.mail_port = mail_port
        self.mail_from_user = mail_from_user
        self.mail_from_passwd = mail_from_passwd
        self.mail_from = mail_from
        self.mail_to = mail_to

    def flush(self):
        """
        缓存存满溢出或者条件满足,执行动作
        """
        if self.buffer != [] and len(self.buffer) >= self.capacity:
            content = ''
            for record in self.buffer:
                message = record.getMessage()
                content += record.levelname + " occurred at " + \
                    time.strftime(
                        '%Y-%m-%d %H:%M:%S', time.localtime(record.created)) + \
                    "  : " + message + " in " + record.pathname + " at line " + str(record.lineno) + '\n'
            self.send_warning_mail(
                self.mail_subject, content, self.mail_host, self.mail_port, self.mail_from_user,
                self.mail_from_passwd, self.mail_from, self.mail_to)
            self.buffer = []

    def send_warning_mail(self, subject, content, host, port, user, passwd, from_addr, to_addr):
        """
        发送邮件
        """
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')  # 标题
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host, port)
            smtp.login(user, passwd)
            smtp.sendmail(from_addr, to_addr, msg.as_bytes())
            smtp.quit()
            print("异常邮件发送成功!")
        except Exception as ex:
            print(ex)
