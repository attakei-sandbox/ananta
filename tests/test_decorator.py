# -*- coding:utf8 -*-
"""Test for Ananta functions registry
"""
from ananta import lambda_function


def test_with_configs():
    @lambda_function(FunctionName='test_plain')
    def _test_with_configs(arg1, arg2):
        return '_test_with_configs'

    assert _test_with_configs(None, None) == '_test_with_configs'


def test_attach_function_name():
    import venusian
    from ananta import Registry
    from . import tests_scan

    registry = Registry()
    scanner = venusian.Scanner(registry=registry)
    scanner.scan(tests_scan)
    assert 'lambda_func_1' in registry.functions
    assert 'my_func_2' in registry.functions
