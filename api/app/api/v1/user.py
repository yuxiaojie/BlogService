from app.api.api_base import ApiBlueprint
from app.component import get_response

api = ApiBlueprint('user')


@api.route('/list/<int:page>/<int:size>', methods=['GET'])
# @verify_token(Permission.ADMIN_FULL_ACCESS, Permission.ADMIN_COMMON_ACCESS, Permission.ADMIN_USER_FULL_ACCESS)
# @page_safe_check
def get_user_list(user, page, size):
    # chan = get_json_data().get(PARAM_CHANNEL, '')
    # phone = get_json_data().get(PARAM_PHONE, '')
    # tag = get_json_data().get(PARAM_TAG, '')
    return get_response('get user list success')
