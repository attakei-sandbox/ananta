# -*- coding:utf8 -*-
"""Ananta : AWS Lambda packager
"""
import functools
import json

__version__ = '0.0.1'


class Registry(object):
    """Lambda functions registry
    """
    def __init__(self):
        self.functions = {}

    def add(self, name, func, params):
        self.functions[name] = {
            'name': name,
            'func': func,
            'params': params,
        }

    def jsonify(self):
        """Return functions as json, to use boto3
        """
        funcs_ = []
        for name, data in self.functions.items():
            funcs_.append({})
        return json.dumps(funcs_)


class FunctionCollector(object):
    """Lambda functions collector
    """
    def __init__(self):
        self._functions = []
        self._defaults = {
            'MemorySize': 128,
            'Description': '',
        }

    def lambda_config(self, func=None, **kwargs):
        """lambda function decorator

        :param name: lambda function name
        :type name: srt or unicode
        :rtype: function
        """
        function = {}
        # Custom values
        if func is not None:
            function['FunctionName'] = func.__name__
        elif 'FunctionName' in kwargs:
            function['FunctionName'] = kwargs['FunctionName']
        # Default values
        function.update(self._defaults)
        # Decorated values
        function.update(kwargs)

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
            if key in ('MemorySize', 'Timeout'):
                self._defaults[key] = int(val)
            else:
                self._defaults[key] = val

_collector = FunctionCollector()


lambda_config = _collector.lambda_config
