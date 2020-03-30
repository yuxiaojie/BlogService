from app.api.api_base import ApiBlueprint
from app.component import get_response

api = ApiBlueprint('user')


@api.route('/list', methods=['GET'])
def page_user_list():
    return 'this is user list'
