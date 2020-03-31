import hashlib
import os
from datetime import datetime

from app.celery_task.celery_utils import celery_print, db_wrapper
from app.config import LOG_PATH
from app.models import Article

REPOSITORY_NAME = 'blog-article'
REPOSITORY = 'git@github.com:yuxiaojie/blog-article.git'
WORKING_DIR = LOG_PATH

main_type = (('技术原创', Article.TYPE_ORIGINAL), ('文章阅读', Article.TYPE_READ), ('生活杂谈', Article.TYPE_FREE))


def get_md5_01(content):
    md5_obj = hashlib.md5()
    md5_obj.update(content)
    hash_code = md5_obj.hexdigest()
    return str(hash_code).lower()


class DbAccess:

    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_article(self):
        return {item[2]: {'sum': item[1], 'id': item[0]}
                for item in self.db_session.query(Article.id, Article.md5_sum, Article.rel_path).all()}

    def add_article(self, rel_path, name, md5_sum, text, article_type):
        self.db_session.add(Article(rel_path, name, md5_sum, text, article_type))

    def update_article(self, aid, md5_sum, text):
        self.db_session.query(Article).filter(Article.id == aid).update(
            {Article.md5_sum: md5_sum, Article.update_time: datetime.now(), Article.text: text})

    def miss_article(self, rel_path):
        self.db_session.query(Article).filter(Article.rel_path == rel_path).update(
            {Article.state: Article.STATE_MISS, Article.update_time: datetime.now()})


@db_wrapper
def gen_article(db_session):

    home = os.path.join(WORKING_DIR, REPOSITORY_NAME)
    update_repo(home)

    db_access = DbAccess(db_session)
    all_article = db_access.get_all_article()
    detected_article = set()
    for t, a_type in main_type:
        for dir_path, _, all_file in os.walk(os.path.join(home, t)):
            for a in all_file:
                if a.endswith('.md'):
                    abs_p = os.path.join(dir_path, a)
                    rel_p = abs_p.split(REPOSITORY_NAME + os.path.sep, maxsplit=2)[1]

                    with open(abs_p, 'rb') as f:
                        content = f.read()
                        file_sum = get_md5_01(content)
                        detected_article.add(rel_p)

                        # 没有这个文章就写入数据库，有就检查sum看文章是否更新
                        if rel_p not in all_article:
                            celery_print('add article {} from {}'.format(a, rel_p))
                            db_access.add_article(rel_p, a, file_sum, content.decode(encoding='utf-8'), a_type)
                        elif all_article[rel_p]['sum'] != file_sum:
                            celery_print('update article {} from {}'.format(a, rel_p))
                            db_access.update_article(all_article[rel_p]['id'], file_sum, content.decode(encoding='utf-8'))

    db_session.commit()

    # 查看数据库中有的但是版本仓库没有的文字，将其置为丢失状态不再展示
    for k in all_article.keys():
        if k not in detected_article:
            celery_print('miss article {}'.format(k))
            db_access.miss_article(k)
    db_session.commit()
    celery_print('gen article complete')


def update_repo(home):

    if not os.path.exists(home):

        cmd = 'cd {} && git clone {}'.format(WORKING_DIR, REPOSITORY)
        celery_print('not find repository on {}, try to clone ... '.format(home))
        celery_print(cmd)
        p = os.popen(cmd)
        cmd_out = p.read()
        code = p.close()
        if code is None:
            celery_print('clone repository success')
        else:
            celery_print('clone repository failed, exit code: {}'.format(code))
            celery_print('std out: {}'.format(cmd_out))
            return
    else:

        cmd = 'cd {} && git pull'.format(home)
        celery_print('detected git home, try to pull ... ')
        celery_print(cmd)
        p = os.popen(cmd)
        cmd_out = p.read()
        code = p.close()
        if code is None:
            celery_print('pull repository success')
        else:
            celery_print('pull repository failed, exit code: {}'.format(code))
            celery_print('std out: {}'.format(cmd_out))


if __name__ == '__main__':
    gen_article()
