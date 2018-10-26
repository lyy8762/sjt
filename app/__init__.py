"""
 Created by 七月 on 2018-2-5.
"""
from flask import Flask
from flask_login import LoginManager
from app.models.book import db
from flask_mail import Mail
from app.libs.limiter import Limiter

__author__ = '七月'

login_manager = LoginManager()
mail = Mail()
# cache = Cache(config={'CACHE_TYPE': 'simple'})
limiter = Limiter()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)

    # RPG 代入感
    # 认同感
    # 移情
    # 同理心
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
