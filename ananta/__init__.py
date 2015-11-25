# -*- coding:utf8 -*-
"""Ananta : AWS Lambda packager
"""
import sys
import functools

__version__ = '0.0.1'


class FunctionCollector(object):
    def __init__(self):
        self._functions = []

    def lambda_config(self, name, **kwargs):
        function = {
            'name': name
        }
        function['role'] = kwargs.get('role')

        def _lambda_reciever(func):
            function['handler'] = '{}.{}'.format(func.__module__.replace('.', '/'), func.__name__)

            @functools.wraps(func)
            def _func(event, context):
                return func(event, context)

            return _func

        self._functions.append(function)
        return _lambda_reciever

    @property
    def functions(self):
        return self._functions

collector_ = FunctionCollector()


lambda_config = collector_.lambda_config


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
