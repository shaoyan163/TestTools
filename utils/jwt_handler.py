# encoding: utf-8

"""
@author: shaoyanyan
@file: jwt_handler.py
@time: 2020/4/9 22:23
@ide: pycharm

"""


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        "user_id": user.id,
        "username": user.username
    }
