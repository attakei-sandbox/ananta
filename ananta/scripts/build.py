# -*- coding:utf8 -*-
"""
"""
from __future__ import unicode_literals
import shutil
import tempfile


__author__ = 'attakei'


def build_packages(registry, config, args):
    import pip
    if args.path is None:
        args.path = tempfile.mkdtemp()
    pip_args = 'install -t {} .'.format(args.path)
    pip.main(pip_args.split(' '))
    shutil.make_archive('package', 'zip', root_dir=args.path)
