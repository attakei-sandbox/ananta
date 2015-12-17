# -*- coding:utf8 -*-
"""
"""
from __future__ import unicode_literals
import shutil


__author__ = 'attakei'


def build_packages(registry, config, args):
    import pip
    pip_args = 'install -t {} .'.format(args.path)
    pip.main(pip_args.split(' '))
    shutil.make_archive('package', 'zip', root_dir=args.path)
