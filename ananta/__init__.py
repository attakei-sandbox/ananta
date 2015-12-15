# -*- coding:utf8 -*-
"""Ananta : AWS Lambda packager
"""
import functools
import json
import venusian

__version__ = '0.0.1'


class Registry(object):
    """Lambda functions registry
    """

    DEFAULTS = {
        'MemorySize': 128,
        'Timeout': 3,
    }

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
            params = {}
            params['FunctionName'] = data['func'].__name__
            for key, value in self.DEFAULTS.items():
                params.setdefault(key, value)
            funcs_.append(params)
        return json.dumps(funcs_)


def lambda_function(**kwargs):
    """lambda function decorator

    :param name: lambda function name
    :type name: srt or unicode
    :rtype: function
    """
    def _lambda_receiver(func):
        def _scan_function(scanner, name, ob):
            name = kwargs.get('FunctionName', name)
            scanner.registry.add(name, ob, kwargs)

        venusian.attach(func, _scan_function)
        return func

    return _lambda_receiver


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
