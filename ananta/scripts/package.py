# -*- coding:utf8 -*-
"""Packaging logics
"""
import sys
import os
import shutil
import tempfile
import json
import importlib
import venusian


def package_sources(args):
    """Package sources, dependencies and functions.json

    * Create packaging workspace
    * Install sources and packages into workspace
    * Dump functions.json into workspace
    * Generate zip archive from workspace
    """
    # from .. import _collector
    from .. import Registry
    if not os.path.exists(os.path.join(os.getcwd(), 'setup.py')):
        print('error')  # TODO: Refactor
        return 1
    package_dir = tempfile.mkdtemp()
    # パッケージの作成
    from pip import main as pip_main
    pip_main(['install', '-t', package_dir, '.'])
    registry = Registry()
    scanner = venusian.Scanner(registry=registry)
    for module in find_modules(package_dir):
        scanner.scan(module)
    print(registry.registered)
    # sys.stdout.write(json.dumps(_collector.functions, ensure_ascii=False))
    shutil.rmtree(package_dir)
    return(0)


def find_modules(package_dir):
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
    return modules
