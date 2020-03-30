
from flask_cors import CORS

from app import init_app_br
from app.base import create_app

app = create_app()
CORS(app, supports_credentials=True)

init_app_br(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2345)
