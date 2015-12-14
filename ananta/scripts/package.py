# -*- coding:utf8 -*-
"""Packaging logics
"""
import os
import tempfile


def package_sources(args):
    """Package sources, dependencies and functions.json

    * Create packaging workspace
    * Install sources and packages into workspace
    * Dump functions.json into workspace
    * Generate zip archive from workspace
    """
    if not os.path.exists(os.path.join(os.getcwd(), 'setup.py')):
        print('error') # TODO: Refactor
        return 1
    package_dir = tempfile.mkdtemp()
    # パッケージの作成
    from pip import main as pip_main
    pip_main(['install', '-t', package_dir, '.'])
    print(package_dir)
    return(0)
