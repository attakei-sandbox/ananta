# -*- coding:utf8 -*-
"""Test for ananta.scripts
"""
from ananta.scripts import parser
from pytest import raises


def test_script_func():
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


class TestForDumpFunction(object):
    def setup_method(self, method):
        import ananta
        ananta.collector_ = ananta.FunctionCollector()
        ananta.lambda_config = ananta.collector_.lambda_config

    def _call_fut(self):
        from ananta.scripts import dump_functions
        return dump_functions

    def _parse_args(self, *args):
        from ananta.scripts import parser
        return parser.parse_args(['dump'] + list(args))

    def test_path_default(self, capsys):
        import json
        args = self._parse_args('-p', 'tests/sampleapp')
        self._call_fut()(args)
        out, err = capsys.readouterr()
        out_data = json.loads(out)
        assert out.startswith('[')
        assert type(out_data) is list
        assert len(out_data) == 1
