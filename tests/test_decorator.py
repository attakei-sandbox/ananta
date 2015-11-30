# -*- coding:utf8 -*-
"""Test for Ananta decorator
"""
from ananta import lambda_config


def test_it():
    @lambda_config(FunctionName='my_func')
    def lambda_func(event, context):
        return {}

    assert lambda_func(None, None) == {}
