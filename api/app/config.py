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

CELERY_IGNORE_RESULT = True
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_TIMEZONE = 'Asia/Shanghai'

ENV = os.environ.get('BLOG_SERVER_ENV', 'dev')
HOST_ID = os.environ.get('HOST_ID', '000')
print('load config, env: ', ENV, ', hostId: ', HOST_ID)


MAX_CONTENT_LENGTH = 200 * 1024 * 1024


if ENV == 'product':
    API_HOST = 'api.jeffyu.cn'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://blog:a5d685d35ee0d5979227f6f79196e6e4' \
                              '@172.16.97.228:3308/blog_db?charset=utf8mb4'
    CELERY_BROKER_URL = 'redis://:009699c95ccd88db10fde88ddaf96c4adc41ffa3f30bf3499c365d936684e336@172.16.97.228:6688/0'
    LOG_PATH = '/var/log/tissue'
    GIT_SSH_COMMAND = 'ssh -i /home/www/.ssh/id_rsa'
else:
    API_HOST = '127.0.0.1:2345'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qwer`1234@localhost:3308/blog_db?charset=utf8mb4'
    CELERY_BROKER_URL = 'redis://:009699c95ccd88db10fde88ddaf96c4adc41ffa3f30bf3499c365d936684e336@127.0.0.1:6688/0'
    LOG_PATH = '/tmp/tissue'
    GIT_SSH_COMMAND = ''


def in_product():
    return ENV == 'product'
