# -*- coding:utf8 -*-
"""Ananta : Console reporting command
"""
import os
import importlib
import venusian


def module_from_path(path):
    current_dir = os.getcwd()
    relative_dir = path.replace(current_dir, '')[1:]
    module_path = relative_dir.replace('/', '.')
    return importlib.import_module(module_path)


def report_functions(registry, args):
    module = module_from_path(args.path)
    scanner = venusian.Scanner(registry=registry)
    scanner.scan(module)
    display_as_test(registry)


def display_as_test(registry):
    for name, function in registry.functions.items():
        params = function['params']
        print('Function : ' + name)
        print('\thandler: ' + params['Handler'])
