from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.base import create_app
from app.config import SQLALCHEMY_DATABASE_URI
from app import models
from app.models.db_base import db

print(SQLALCHEMY_DATABASE_URI)
app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)  # 注册migrate到flask

manager.add_command('db', MigrateCommand)   # 在终端环境下添加一个db命令

if __name__ == '__main__':
    manager.run()
