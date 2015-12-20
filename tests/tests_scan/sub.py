# -*- coding:utf8 -*-
"""decorated functions test_scan
"""
from ananta import lambda_function


@lambda_function()
def lambda_func_1(event, context):
    return {}


@lambda_function(FunctionName='my_func_2')
def lambda_func_2(event, context):
    return {}
