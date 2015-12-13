# -*- coding:utf8 -*-
"""Packaging logics
"""
import os
import tempfile
import shutil
import zipfile


def package_sources(args):
    """Package sources, dependencies and functions.json

    * Create packaging workspace
    * Install sources and packages into workspace
    * Dump functions.json into workspace
    * Generate zip archive from workspace
    """
    package_dir = tempfile.mkdtemp()
    functions_dump_path = os.path.join(package_dir, 'functions.json')
    with open(functions_dump_path, 'w') as fp:
        from .dump import dump_functions
        dump_functions(args, fp)
    # パッケージの作成
    package_file = './minimum_arc.zip'
    with zipfile.ZipFile(package_file, 'w') as zfp:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                if file.endswith('.pyc'):
                    continue
                fullpath = os.path.join(root, file)
                itempath = fullpath.replace(package_dir+'/', '')
                zfp.write(fullpath, itempath)
    shutil.rmtree(package_dir)
