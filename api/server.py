
from flask_cors import CORS

from app import init_app_br
from app.base import create_app
from app.models.db_base import db

app = create_app()
CORS(app, supports_credentials=True)

init_app_br(app)
db.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2345)
