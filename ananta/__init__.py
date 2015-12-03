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
        self._defaults = {
            'MemorySize': 128,
        }

    def lambda_config(self, func=None, **kwargs):
        """lambda function decorator

        :param name: lambda function name
        :type name: srt or unicode
        :rtype: function
        """
        function = {}
        if func is not None:
            function['FunctionName'] = func.__name__
        elif 'FunctionName' in kwargs:
            function['FunctionName'] = kwargs['FunctionName']
        function['Role'] = kwargs.get('Role', self._defaults.get('Role'))
        function['Description'] = kwargs.get('Description', self._defaults.get('Description', ''))
        for k, v in self._defaults.items():
            function.setdefault(k, v)

        def _lambda_reciever(func):
            function['Handler'] = '{}.{}'.format(func.__module__.replace('.', '/'), func.__name__)

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
        for key, val in config.items('ananta'):
            self._defaults[key] = val

_collector = FunctionCollector()


lambda_config = _collector.lambda_config
