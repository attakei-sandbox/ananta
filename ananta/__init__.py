# -*- coding:utf8 -*-
"""Ananta : AWS Lambda packager
"""
from __future__ import unicode_literals
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
        self._defaults = {}

    def set_default(self, key, value):
        self._defaults[key] = value

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
            params = data['params']
            params.setdefault('FunctionName', data['func'].__name__)
            for key, value in self._defaults.items():
                params.setdefault(key, value)
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
        kwargs.setdefault('FunctionName', func.__name__)
        kwargs['Handler'] = '{}.{}'.format(func.__module__.replace('.', '/'), func.__name__)

        def _scan_function(scanner, name, ob):
            scanner.registry.add(kwargs.get('FunctionName', name), ob, kwargs)

        venusian.attach(func, _scan_function)
        return func

    return _lambda_receiver


lambda_config = lambda_function
