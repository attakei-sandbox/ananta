# -*- coding:utf8 -*-
"""
"""
from __future__ import unicode_literals
import sys
import os
import tempfile


__author__ = 'attakei'


def report_functions(registry, config, args):
    import pip
    import venusian
    import importlib
    if args.path is None:
        package_dir = tempfile.mkdtemp()
    else:
        package_dir = args.path
    pip_args = 'install -t {} .'.format(package_dir)
    pip.main(pip_args.split(' '))
    import glob
    modules = []
    sys.path.append(package_dir)
    for path in glob.glob(os.path.join(package_dir, '*')):
        if os.path.isdir(path) and os.path.exists(os.path.join(path, '__init__.py')):
            module_name = os.path.basename(path)
        elif path.endswith('.py'):
            module_name = os.path.basename(path)[:-3]
        else:
            continue
        modules.append(importlib.import_module(module_name))
    scanner = venusian.Scanner(registry=registry)
    for module in modules:
        scanner.scan(module)
    # shutil.make_archive('package', 'zip', root_dir=args.path)
    display_as_test(registry.jsonify())


def display_as_test(json_data):
    import json
    for function in json.loads(json_data):
        print('Function : ' + function['FunctionName'])
        for key, val in function.items():
            print('\t{}: {}'.format(key, val))
