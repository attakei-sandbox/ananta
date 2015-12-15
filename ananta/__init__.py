# -*- coding:utf8 -*-
"""Ananta : AWS Lambda packager
"""
import venusian

__version__ = '0.0.1'


class Registry(object):
    def __init__(self):
        self.registered = []

    def add(self, name, ob):
        self.registered.append((name, ob))


def lambda_config(func, **kwargs):
    function = {}
    if func is not None:
        function['FunctionName'] = func.__name__
    elif 'FunctionName' in kwargs:
        function['FunctionName'] = kwargs['FunctionName']

    def _lambda_receiver(scanner, name, ob):
        def _func(event, context):
            return func(event, context)

        scanner.registry.add(name, function)

    venusian.attach(func, _lambda_receiver)
    return func

# def lambda_config(func=None, **kwargs):
#     """lambda function decorator
#
#     :param name: lambda function name
#     :type name: srt or unicode
#     :rtype: function
#     """
#     function = {}
#     # Custom values
#     if func is not None:
#         function['FunctionName'] = func.__name__
#     elif 'FunctionName' in kwargs:
#         function['FunctionName'] = kwargs['FunctionName']
#     # Default values
#     # function.update(self._defaults)
#     # Decorated values
#     function.update(kwargs)
#
#     def _lambda_reciever(scanner, func):
#         function['Handler'] = '{}.{}'.format(func.__module__.replace('.', '/'), func.__name__)
#
#         @functools.wraps(func)
#         def _func(event, context):
#             return func(event, context)
#
#         scanner.registry.add(name, jsonified)
#         # return _func
#
#     venusian.attach(func, _lambda_reciever)
#     # self._functions.append(function)
#     return _lambda_reciever
#
