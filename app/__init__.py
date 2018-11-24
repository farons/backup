from flask import Flask, render_template
from config import config


def create_app(config_name):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 注册蓝图
    from .main import view_modules as buleprint_modules 
    for key in buleprint_modules:
        app.register_blueprint(key,url_prefix=buleprint_modules[key])


    return app