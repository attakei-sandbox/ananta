# -*- coding:utf8 -*-
"""Ananta : Console scripts
"""
import os
import sys
import argparse
import json


def dump_functions(args):
    """Scan functions decorated by lambda_config, and dump as json
    """
    import importlib
    import venusian
    from ananta import collector_
    args.path = os.path.abspath(args.path)
    module_path = args.path.replace(os.getcwd()+'/', '')
    module_name = module_path.replace('/', '.')
    module = importlib.import_module(module_name)
    scanner = venusian.Scanner()
    scanner.scan(module)
    print(json.dumps(collector_.functions))


def directory_path(arg):
    abs_arg = os.path.abspath(arg)
    if not os.path.exists(abs_arg):
        msg = "%r is not exists" % arg
        raise argparse.ArgumentTypeError(msg)
    if not os.path.isdir(abs_arg):
        msg = "%r is not directory path" % arg
        raise argparse.ArgumentTypeError(msg)
    return abs_arg


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')
parser_dump = subparsers.add_parser('dump', help='dump as YAML')
parser_dump.set_defaults(func=dump_functions)
parser_dump.add_argument('-p', '--path', type=directory_path, required=True, help='target module path')


def main(argv=None):
    """Console script endpoint

    :param args: console arguments
    :type args: list
    :returns: console return code
    :rtype: int
    """
    if argv is None:
        argv = sys.argv[1:]
    args = parser.parse_args(argv)
    return args.func(args)
