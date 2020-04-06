# encoding: utf-8

"""
@author: shaoyanyan
@file: pagination.py
@time: 2020/4/6 20:12
@ide: pycharm

"""
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = "p"
    page_size = 2
    page_query_param = "page"
    max_page_size = 50