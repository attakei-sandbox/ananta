# -*- coding:utf8 -*-
"""Test for Ananta functions registry
"""
import json
from ananta import Registry


def test_structures():
    registry = Registry()

    assert type(registry.functions) is dict

    def _test_structures(arg1, arg2):
        pass

    registry.add('func_name', _test_structures, {})
    assert len(registry.functions) == 1


class TestForJsonify(object):
    def test_none(self):
        registry = Registry()
        json_string = registry.jsonify()
        assert type(json_string) is str
        loaded = json.loads(json_string)
        assert type(loaded) is list

    def test_single_added(self):
        registry = Registry()

        def _test_structures(arg1, arg2):
            pass

        registry.add('func_name', _test_structures, {})
        loaded = json.loads(registry.jsonify())
        assert type(loaded[0]) is dict
        assert loaded[0]['FunctionName'] == '_test_structures'

        def _test_structures2(arg1, arg2):
            pass

        registry.add('func_name', _test_structures2, {})
        loaded = json.loads(registry.jsonify())
        assert loaded[0]['FunctionName'] == '_test_structures2'

    def test_has_default(self):
        registry = Registry()

        def _test_structures(arg1, arg2):
            pass

        registry.add('func_name', _test_structures, {})
        loaded = json.loads(registry.jsonify())
        assert loaded[0]['MemorySize'] == 128
        assert loaded[0]['Timeout'] == 3
