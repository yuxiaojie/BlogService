import logging
import multiprocessing
import os
from logging.handlers import WatchedFileHandler

from app.config import LOG_PATH

user = 'www'
group = 'www'

debug = False
deamon = False
loglevel = 'info'
bind = '0.0.0.0:12345'
max_requests = 5000

x_forwarded_for_header = "X-Real-IP"

# 启动的进程数
workers = multiprocessing.cpu_count()
# workers = 3
worker_class = "gevent"

accesslog = '/dev/null'
access_log_format = '%({X-Real-IP}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = '/dev/null'

timeout = 60

access_log = logging.getLogger('gunicorn.access')
access_log.addHandler(WatchedFileHandler(os.path.join(LOG_PATH, 'access.log')))

error_log = logging.getLogger('gunicorn.error')
error_log.addHandler(WatchedFileHandler(os.path.join(LOG_PATH, 'error.log')))
