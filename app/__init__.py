from flask import Flask, render_template


def create_app(config_name=None):
    app = Flask(__name__)
    
    # 注册蓝图
    from .main import view_modules as buleprint_modules 
    for key in buleprint_modules:
        app.register_blueprint(key,url_prefix=buleprint_modules[key])

    return app
