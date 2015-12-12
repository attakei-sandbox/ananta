# -*- coding:utf8 -*-
"""Test for ananta.scripts
"""
import os
import sys
from pytest import raises
from . import working_directory, test_dir, samples_dir


def test_script_func():
    from ananta.scripts import parser
    raises(SystemExit, parser.parse_args, [])


# def test_dump_functions_main(capsys):
#     from ananta.scripts import dump_functions
#     import json
#     args = parser.parse_args(['dump', '-p', './sss'])
#     dump_functions(args)
#     out, err = capsys.readouterr()
#     assert out.startswith('[')
#     assert type(json.loads(out)) is list


class TestForDumpParser(object):
    def _call_fut(self):
        from ananta.scripts import parser_dump
        return parser_dump

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
        from ananta.scripts.dump import dump_functions
        return dump_functions

    def _parse_args(self, args):
        from ananta.scripts import parser
        args.insert(0, 'dump')
        return parser.parse_args(args)

    def _run_script(self, capsys, args):
        import json
        with working_directory(os.path.join(test_dir, 'samples')):
            args = self._parse_args(args)
            self._call_fut()(args)
            out, err = capsys.readouterr()
        return json.loads(out)

    def test_it(self, capsys):
        out_data = self._run_script(capsys, ['-p', 'minimum'])
        assert type(out_data) is list
        assert len(out_data) == 1
        assert out_data[0]['FunctionName'] == 'test_funcs'
        assert out_data[0]['Description'] == ''

    def test_with_name(self, capsys):
        out_data = self._run_script(capsys, ['-p', 'singlefunction'])
        assert type(out_data) is list
        assert len(out_data) == 1
        assert out_data[0]['MemorySize'] == 128

    def test_spec_config(self, capsys):
        out_data = self._run_script(
            capsys,
            ['-p', 'with_config', '-c', 'with_config/ananta_conf.ini']
        )
        assert type(out_data) is list
        assert out_data[0]['Role'] == 'arn:aws:iam::account-id:role/role-name'
        assert 'FunctionName' in out_data[0]
        assert 'Role' in out_data[0]
        assert 'role' not in out_data[0]
