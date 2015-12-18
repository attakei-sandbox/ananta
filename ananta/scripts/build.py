# -*- coding:utf8 -*-
"""
"""
from __future__ import unicode_literals
import os
import glob
import shutil
import importlib
import tempfile


__author__ = 'attakei'


def build_packages(registry, config, args):
    import pip
    if args.path is None:
        args.path = tempfile.mkdtemp()
    pip_args = 'install -t {} .'.format(args.path)
    pip.main(pip_args.split(' '))
    scan_all(registry, args.path)
    shutil.make_archive('package', 'zip', root_dir=args.path)


def scan_all(registry, package_dir):
    import venusian
    modules = []
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
    with open(os.path.join(package_dir, 'functions.json'), 'w') as fp:
        fp.write(registry.jsonify())
