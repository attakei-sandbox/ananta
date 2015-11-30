# -*- coding:utf8 -*-
"""
"""
from ananta import lambda_config


@lambda_config(Name='test_1')
def test_funcs(event, context):
    return {}
