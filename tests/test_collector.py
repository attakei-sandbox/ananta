# -*- coding:utf8 -*-
"""Test for Ananta decorator
"""
from ananta import FunctionCollector


def test_structures():
    lambda_collection = FunctionCollector()

    @lambda_collection.lambda_config(name='my_func')
    def lambda_func(event, context):
        return {}

    assert len(lambda_collection.functions) == 1
    assert type(lambda_collection.functions) == list


def test_required():
    lambda_collection = FunctionCollector()

    @lambda_collection.lambda_config(name='my_func', role='arn:aws:::::dummy')
    def lambda_func(event, context):
        return {}

    decorated = lambda_collection.functions[0]
    assert decorated['name'] == 'my_func'
    assert decorated['handler'] == 'tests/test_collector.lambda_func'
    assert decorated['role'] == 'arn:aws:::::dummy'
