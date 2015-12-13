# -*- coding:utf8 -*-
"""Dump logics
"""
import sys
import os
import json
import importlib
import ConfigParser
import venusian


def dump_functions(args, stream=None):
    """Scan functions decorated by lambda_config, and dump as json
    """
    from ananta import _collector
    if args.conf is not None:
        config = ConfigParser.SafeConfigParser()
        config.optionxform = str
        config.read(args.conf)
        _collector.set_defaults(config)
    module_path = args.path.replace(os.getcwd()+'/', '')
    module_name = module_path.replace('/', '.')
    module = importlib.import_module(module_name)
    scanner = venusian.Scanner()
    scanner.scan(module)
    if stream is None:
        stream = sys.stdout
    stream.write(json.dumps(_collector.functions, ensure_ascii=False))
