# -*- coding:utf8 -*-
"""Test for Ananta functions registry
"""
from ananta import lambda_function


def test_with_configs():
    @lambda_function(FunctionName='test_plain')
    def _test_with_configs(arg1, arg2):
        return '_test_with_configs'

    assert _test_with_configs(None, None) == '_test_with_configs'
