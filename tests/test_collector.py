# -*- coding:utf8 -*-
"""Test for Ananta decorator
"""
from ananta import FunctionCollector


lambda_collection = FunctionCollector()


def test_it():
    @lambda_collection.lambda_config
    def lambda_func(event, context):
        return {}

    assert len(lambda_collection.functions) == 1
