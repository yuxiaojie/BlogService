from app.api.api_base import ApiBlueprint
from app.celery_task import gen_article
from app.component import get_response

api = ApiBlueprint('callback')


@api.route('/github/update-article', methods=['GET'])
def update_article():
    # 6f2658fb07626ec9612dc8069d440266
    gen_article.delay()
    return 'success'
