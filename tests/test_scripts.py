# -*- coding:utf8 -*-
"""Test for ananta.scripts
"""
from ananta.scripts import parser
import unittest
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


class TestForDumpParser(unittest.TestCase):
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


# class TestForDumpFunction(unittest.TestCase):
#     def _call_fut(self):
#         from ananta.scripts import dump_functions
#         return dump_functions
#
#     def _parse_args(self, argv=None):
#         from ananta.scripts import parser
#         if argv is None:
#             argv = []
#         return parser.parse_args(['dump'] + argv)
#
#     def test_path_default(self):
#         args = self._parse_args()
#         assert args.path != ''
