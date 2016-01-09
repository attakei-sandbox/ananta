# -*- coding:utf8 -*-
"""
"""
from __future__ import unicode_literals
import sys
import os
import glob
import shutil
import importlib
import tempfile


__author__ = 'attakei'


def build_packages(registry, config, args):
    import pip
    for key, val in config.items('ananta:function'):
        registry.set_default(key, val)
    if args.path is None:
        args.path = tempfile.mkdtemp()
    pip_args = 'install -t {} .'.format(args.path)
    pip.main(pip_args.split(' '))
    target = config.get('ananta:build', 'target')
    scan_all(registry, args.path, target)
    shutil.make_archive('package', 'zip', root_dir=args.path)


def scan_all(registry, package_dir, target=None):
    import venusian
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
    if target:
        target_modules = [t.strip() for t in target.split('\n') if t != '']
        modules = [module for module in modules if module.__name__ in target_modules]
    scanner = venusian.Scanner(registry=registry)
    for module in modules:
        scanner.scan(module)
    with open(os.path.join(package_dir, 'functions.json'), 'w') as fp:
        fp.write(registry.jsonify())
