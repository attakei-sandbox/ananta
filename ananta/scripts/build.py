# -*- coding:utf8 -*-
"""
"""
from __future__ import unicode_literals


__author__ = 'attakei'


def build_packages(registry, config, args):
    import pip
    pip_args = 'install -t {} .'.format(args.path)
    print(pip_args)
    pip.main(pip_args.split(' '))
