from flask import Flask, render_template
from config import config


def app_create(config_name):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 注册蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app