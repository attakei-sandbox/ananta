# -*- coding:utf8 -*-
"""
"""
from ananta import lambda_config


@lambda_config(FunctionName='test_1')
def test_funcs(event, context):
    return {}
