# -*- coding:utf8 -*-
"""Ananta : AWS Lambda packager
"""
import sys
import functools

__version__ = '0.0.1'


def lambda_config(func):
    """Basic AWS-Lambda function defination decorator
    """

    @functools.wraps(func)
    def _decorator(event, context):
        return func(event, context)

    return _decorator


class FunctionCollector(object):
    def __init__(self):
        self._functions = []

    def lambda_config(self, func):
        func_path = '{}.{}'.format(func.__module__, func.__name__)
        self._functions.append(func_path)

        @functools.wraps(func)
        def _decorator(event, context):
            return func(event, context)

        return _decorator

    @property
    def functions(self):
        return self._functions


def main(args=None):
    """Console script endpoint

    :param args: console arguments
    :type args: list
    :returns: console return code
    :rtype: int
    """
    if args is None:
        args = sys.argv
    return 0
