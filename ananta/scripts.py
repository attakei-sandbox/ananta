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
    from ananta import _collector
    args.path = os.path.abspath(args.path)
    module_path = args.path.replace(os.getcwd()+'/', '')
    module_name = module_path.replace('/', '.')
    module = importlib.import_module(module_name)
    scanner = venusian.Scanner()
    scanner.scan(module)
    sys.stdout.write(json.dumps(_collector.functions))


def directory_path(arg):
    """ArgumentParser type. It check if arg is exists directory path.

    :param arg: console argument
    :type arg: srt or unicode
    :returns: absolute path
    :rtype: str or unicode
    :raises: argparse.ArgumentTypeError
    """
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
