
from celery_worker import app

from .doc import gen_article

gen_article = app.task(gen_article, ignore_result=True)

