# -*- coding:utf8 -*-
"""Ananta : AWS Lambda packager
"""
import functools

__version__ = '0.0.1'


class FunctionCollector(object):
    """Lambda functions collector
    """
    def __init__(self):
        self._functions = []
        self._defaults = {}

    def lambda_config(self, name, **kwargs):
        """lambda function decorator

        :param name: lambda function name
        :type name: srt or unicode
        :rtype: function
        """
        function = {
            'name': name
        }
        function['role'] = kwargs.get('role', self._defaults.get('role'))

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

    def set_defaults(self, config):
        self._defaults['role'] = config.get('ananta', 'role')

_collector = FunctionCollector()


lambda_config = _collector.lambda_config
