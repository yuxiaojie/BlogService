from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.mysql import MEDIUMTEXT

from app.models.db_base import Base


class Article(Base):
    __tablename__ = 'article'
    __table_args__ = {'extend_existing': True}

    STATE_READY = 0
    STATE_ONLINE = 1
    STATE_MISS = 2
    STATE_REMOVE = 3

    TYPE_ORIGINAL = 1
    TYPE_READ = 2
    TYPE_FREE = 3

    id = Column(Integer, primary_key=True, nullable=False)
    rel_path = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(100), default='', nullable=False)
    show_name = Column(String(100), default='', nullable=False)
    md5_sum = Column(String(100), nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)
    desc = Column(String(255), default='', nullable=False)
    article_type = Column(Integer, nullable=False)
    cover = Column(String(50), default='', nullable=False)
    state = Column(Integer, default=0, nullable=False)
    text = Column(MEDIUMTEXT, default='', nullable=False)

    def __init__(self, rel_path, name, md5_sum, text, article_type):
        self.rel_path = rel_path
        self.name = name
        self.show_name = name
        self.md5_sum = md5_sum
        self.text = text
        self.create_time = datetime.now()
        self.update_time = self.create_time
        self.article_type = article_type
