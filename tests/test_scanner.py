# -*- coding:utf8 -*-
"""Test for Ananta scanning
"""
from ananta import FunctionCollector


lambda_collection = FunctionCollector()
lambda_config = lambda_collection.lambda_config


def test_scan():
    import venusian
    from . import tests_scan
    scanner = venusian.Scanner()
    scanner.scan(tests_scan)
    assert len(lambda_collection.functions) == 2
    assert lambda_collection.functions[0]['FunctionName'] in ('my_func_1', 'my_func_2')
