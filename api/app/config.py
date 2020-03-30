import os

VERSION_CODE = 1
VERSION_STRING = '1.0.0'

DEBUG = False
APP_SECRET = 'fdbb9909dc1142b094693a74a5e0bbc28bb7908159d4e71cadf6e390ca227737'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_RECORD_QUERIES = False
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_MAX_OVERFLOW = 30
SQLALCHEMY_POOL_RECYCLE = 600


ENV = os.environ.get('BLOG_SERVER_ENV', 'dev')
HOST_ID = os.environ.get('HOST_ID', '000')
print('load config, env: ', ENV, ', hostId: ', HOST_ID)


MAX_CONTENT_LENGTH = 200 * 1024 * 1024


if ENV == 'product':
    API_HOST = 'api.jeffyu.cn'
    SQLALCHEMY_DATABASE_URI = ''
else:
    API_HOST = '127.0.0.1:2345'
    SQLALCHEMY_DATABASE_URI = ''


def in_product():
    return ENV == 'product'
