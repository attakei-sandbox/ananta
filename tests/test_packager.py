# -*- coding:utf8 -*-
"""Test for ananta.scripts
"""
import os
import sys
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


class TestForDumpFunction(object):
    def setup_method(self, method):
        import ananta
        ananta._collector = ananta.FunctionCollector()
        ananta.lambda_config = ananta._collector.lambda_config
        sys.path.append(os.path.join(test_dir, 'samples'))

    def teardown_method(self, method):
        import sys
        sys.path = sys.path[0:-1]

    def _call_fut(self):
        from ananta.scripts.package import package_sources
        return package_sources

    def _parse_args(self, args):
        from ananta.scripts import parser
        args.insert(0, 'package')
        return parser.parse_args(args)

    def _run_script(self, args):
        with working_directory(os.path.join(test_dir, 'samples')):
            args = self._parse_args(args)
            self._call_fut()(args)

    def test_it(self):
        self._run_script(['-p', 'minimum_arc'])
        test_path = os.path.join(test_dir, 'samples')
        assert os.path.exists(os.path.join(test_path, 'minimum_arc.zip')) is True
