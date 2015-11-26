# -*- coding:utf8 -*-
"""Test for ananta.scripts
"""
from ananta.scripts import parser
from pytest import raises


def test_script_func():
    raises(SystemExit, parser.parse_args, [])


def test_dump_functions_args():
    parsed_args = parser.parse_args(['dump'])
    assert 'func' in parsed_args
