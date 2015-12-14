# -*- coding:utf8 -*-
"""Ananta : Console scripts
"""
import os
import sys
import argparse
import json
import ConfigParser
from .package import package_sources

def dump_functions(args):
    """Scan functions decorated by lambda_config, and dump as json
    """
    import importlib
    import venusian
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
    sys.stdout.write(json.dumps(_collector.functions, ensure_ascii=False))


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


def file_path(arg):
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
    if os.path.isdir(abs_arg):
        msg = "%r is directory path" % arg
        raise argparse.ArgumentTypeError(msg)
    return abs_arg


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')
parser_dump = subparsers.add_parser('dump', help='dump as YAML')
parser_dump.set_defaults(func=dump_functions)
parser_dump.add_argument('-p', '--path', type=directory_path, required=True, help='target module path')
parser_dump.add_argument('-c', '--conf', type=file_path, help='config file path')
parser_package = subparsers.add_parser('package', help='dump as YAML')
parser_package.set_defaults(func=package_sources)
parser_package.add_argument('-c', '--conf', type=file_path, help='config file path')


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
