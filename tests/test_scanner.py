# -*- coding:utf8 -*-
"""Test for Ananta scanning
"""
from ananta import Registry


# lambda_collection = FunctionCollector()
# lambda_config = lambda_collection.lambda_config


def test_scan():
    import venusian
    from . import tests_scan
    registry = Registry()
    scanner = venusian.Scanner(registry=registry)
    scanner.scan(tests_scan)
    assert len(registry) == 2
    assert registry.registered[0][0]['FunctionName'] in ('my_func_1', 'my_func_2')
