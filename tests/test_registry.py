# -*- coding:utf8 -*-
"""Test for Ananta functions registry
"""
from ananta import Registry


def test_structures():
    registry = Registry()

    assert type(registry.functions) is dict

    def _test_structures(arg1, arg2):
        pass

    registry.add('func_name', _test_structures, {})
    assert len(registry.functions) == 1
