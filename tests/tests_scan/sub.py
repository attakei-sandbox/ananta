# -*- coding:utf8 -*-
"""decorated functions test_scan
"""
from ..test_scanner import lambda_config


@lambda_config(name='my_func_1')
def lambda_func_1(event, context):
    return {}


@lambda_config(name='my_func_2')
def lambda_func_2(event, context):
    return {}
