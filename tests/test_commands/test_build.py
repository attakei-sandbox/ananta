# -*- coding:utf8 -*-
"""Test for build command
"""
import os
import shutil
from .. import working_directory, samples_dir
from . import test_dir


__author__ = 'attakei'


class DictObject(dict):
    def __getattr__(self, item):
        return self.get(item, None)


class TestForBuild(object):
    target = os.path.join(test_dir, 'target')

    def setup_method(self, method):
        shutil.rmtree(self.target, ignore_errors=True)
        os.makedirs(self.target)

    def _call_fut(self, args):
        from ananta.scripts.build import build_packages
        return build_packages(None, None, args)

    # def test_not_setup(self):
    #     args = DictObject(path=self.target)
    #     with working_directory(os.path.dirname(__file__)):
    #         self._call_fut(args)

    def test_with_setup(self):
        test_package = os.path.join(samples_dir, 'minimum')
        package_path = os.path.join(test_package, 'package.zip')
        shutil.rmtree(package_path, ignore_errors=True)
        with working_directory(test_package):
            args = DictObject(path=self.target)
            self._call_fut(args)
        assert os.path.exists(package_path)
