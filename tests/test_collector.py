# -*- coding:utf8 -*-
"""Test for Ananta decorator
"""
from ananta import FunctionCollector


def test_structures():
    lambda_collection = FunctionCollector()

    @lambda_collection.lambda_config(Name='my_func')
    def lambda_func(event, context):
        return {}

    assert len(lambda_collection.functions) == 1
    assert type(lambda_collection.functions) == list


def test_required():
    lambda_collection = FunctionCollector()

    @lambda_collection.lambda_config(Name='my_func', Role='arn:aws:::::dummy')
    def lambda_func(event, context):
        return {}

    decorated = lambda_collection.functions[0]
    assert decorated['Name'] == 'my_func'
    assert decorated['Handler'] == 'tests/test_collector.lambda_func'
    assert decorated['Role'] == 'arn:aws:::::dummy'


def test_defaults():
    from ConfigParser import SafeConfigParser
    config = SafeConfigParser()
    config.add_section('ananta')
    config.set('ananta', 'Role', 'test-role')
    lambda_collection = FunctionCollector()
    lambda_collection.set_defaults(config)

    @lambda_collection.lambda_config(Name='my_func')
    def lambda_func(event, context):
        return {}

    decorated = lambda_collection.functions[0]
    assert decorated['Role'] == 'test-role'
