from app.api.api_base import ApiBlueprint
from app.celery_task import gen_article

api = ApiBlueprint('callback')


@api.route('/github/update-article', methods=['GET', 'POST'])
def update_article():
    # 6f2658fb07626ec9612dc8069d440266
    gen_article.delay()
    return 'success'
