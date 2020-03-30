import time

from flask import jsonify, request

from app.base import JSONEncoder
from app.config import in_product


def get_json_data():

    """
        将flask中json和form的参数都打包在一起进行获取
    :return:
    """

    if 'union_json_data' not in request.__dict__:
        json_data = request.get_json() if request.get_json() else {}
        try:
            assert type(json_data) is dict
        except AssertionError:
            json_data = {}
        json_data.update({k: v for k, v in request.values.items()})
        request.__dict__['union_json_data'] = json_data
        return json_data
    else:
        return request.__dict__['union_json_data']


def get_response(message='', error_code=0, data=None):

    """
        响应客户端通用json格式
    :param error_code: 错误代码，默认为0表示成功
    :param message: 响应消息
    :param data: 响应数据
    :return:
    """

    resp_map = {
        "errorCode": error_code,
        "message": message,
        "serverTime": int(time.time() * 1000),
        "data": data,
    }

    resp = JSONEncoder().encode({k: v for k, v in resp_map.items() if k != 'data'} if in_product() else resp_map)
    # logger.api_logger.info('Request Path: %s, Params: %s \nResponse: %s', request.path, get_json_data(), resp)
    if not in_product():
        print('Request Path: %s, Params: %s \nResponse: %s' % (request.path, get_json_data(), resp))
    return jsonify(resp_map)
