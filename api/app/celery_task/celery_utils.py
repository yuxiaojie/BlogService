from datetime import datetime
from functools import wraps
from traceback import print_exception

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import SQLALCHEMY_DATABASE_URI


def celery_print(log):
    print('[{}] {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), log))


class Atomic(object):
    _engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False,
                            pool_size=30, pool_recycle=360, pool_timeout=20, max_overflow=50)
    _session = sessionmaker(bind=_engine, autoflush=False, expire_on_commit=False)

    _err_info = {}

    def __init__(self):
        self.db = self._session()

    def __enter__(self):
        return self.db

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def close(self):
        self.db.close()

    def __exit__(self, exc_typ, exc_val, tb):

        if exc_typ:
            self.rollback()
            self.close()
            print_exception(exc_typ, exc_val, tb)
        else:
            self.commit()
            self.close()

        return True


def db_wrapper(func):
    @wraps(func)
    def wrapper_fun(*args, **kwargs):
        with Atomic() as db:
            kwargs['db_session'] = db
            c = func(*args, **kwargs)
            return c
    return wrapper_fun
