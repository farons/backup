from flask import Flask
from flask import render_template

from config import Config
from app.extensions import config_extentions
from app.main import config_blueprint


def create_app(pro_name, template_folder):
    app = Flask(pro_name, instance_relative_config=True,
                template_folder=template_folder)
    app.config.from_object(Config)
    app.config.from_pyfile('config.py')
    config_extentions(app)
    config_blueprint(app)
    errors(app)
    return app


def errors(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/error.html', error=e)

    @app.errorhandler(500)
    def server_error(e):
        return render_template('errors/error.html', error=e)
