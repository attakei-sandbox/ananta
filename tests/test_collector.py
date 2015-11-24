# -*- coding:utf8 -*-
"""Test for Ananta decorator
"""
from ananta import FunctionCollector


lambda_collection = FunctionCollector()


def test_it():
    @lambda_collection.lambda_config(name='my_func')
    def lambda_func(event, context):
        return {}

    assert len(lambda_collection.functions) == 1
    assert type(lambda_collection.functions) == list
    assert lambda_collection.functions[0]['name'] == 'my_func'
    assert lambda_collection.functions[0]['handler'] == 'tests/test_collector.lambda_func'
