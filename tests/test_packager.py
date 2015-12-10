# -*- coding:utf8 -*-
"""Test for ananta.scripts
"""
# import os
# import sys
from pytest import raises
from . import working_directory, test_dir, samples_dir


class TestForPackageParser(object):
    def _call_fut(self):
        from ananta.scripts import parser_package
        return parser_package

    def test_path_required(self):
        raises(SystemExit, self._call_fut().parse_args, [])

    def test_path_is_not_directory(self):
        raises(SystemExit, self._call_fut().parse_args, ['-p', 'not_found'])
        raises(SystemExit, self._call_fut().parse_args, ['-p', 'README.rst'])

    def test_path_is_directory(self):
        parsed = self._call_fut().parse_args(['-p', 'tests'])
        assert parsed.path[0] == '/'

    def test_config_is_not_found(self, capsys):
        with working_directory(samples_dir):
            raises(SystemExit, self._call_fut().parse_args, ['-p', 'with_config', '-c', 'not_found'])
