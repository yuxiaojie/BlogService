

from flask import Blueprint


def init_app_br(app):

    from app.api.v1 import user

    api = Blueprint('api', __name__)
    user.api.register(api)

    app.register_blueprint(api, url_prefix='/api')

    from app.page import user

    page = Blueprint('page', __name__)
    user.api.register(page)

    app.register_blueprint(page, url_prefix='/')
