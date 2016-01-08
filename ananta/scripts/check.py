# -*- coding:utf8 -*-
"""Ananta : Console reporting command
"""
from __future__ import unicode_literals
import os
import importlib
import venusian


def module_from_path(path):
    current_dir = os.getcwd()
    relative_dir = path.replace(current_dir, '')[1:]
    module_path = relative_dir.replace('/', '.')
    return importlib.import_module(module_path)


def check_functions(registry, config, args):
    if config is not None:
        for key, val in config.items('ananta:function'):
            registry.set_default(key, val)
    module = module_from_path(args.path)
    scanner = venusian.Scanner(registry=registry)
    scanner.scan(module)
    display_as_test(registry.jsonify())


def display_as_test(json_data):
    import json
    for function in json.loads(json_data):
        print('Function : ' + function['FunctionName'])
        for key, val in function.items():
            print('\t{}: {}'.format(key, val))
