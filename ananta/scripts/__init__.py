# -*- coding:utf8 -*-
"""Ananta : Console scripts
"""
import os
import sys
import argparse
import ConfigParser

from .check import check_functions
from .build import build_packages
from .report import report_functions
from .. import Registry
# def dump_functions(args):
#     """Scan functions decorated by lambda_config, and dump as json
#     """
#     import importlib
#     import venusian
#     from ananta import _collector
#     if args.conf is not None:
#         config = ConfigParser.SafeConfigParser()
#         config.optionxform = str
#         config.read(args.conf)
#         _collector.set_defaults(config)
#     module_path = args.path.replace(os.getcwd()+'/', '')
#     module_name = module_path.replace('/', '.')
#     module = importlib.import_module(module_name)
#     scanner = venusian.Scanner()
#     scanner.scan(module)
#     sys.stdout.write(json.dumps(_collector.functions, ensure_ascii=False))


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
parser.add_argument('-c', '--conf', type=file_path, help='config file path')

parser_check = subparsers.add_parser('check', help='Check handler functions')
parser_check.set_defaults(func=check_functions)
parser_check.add_argument('-p', '--path', type=directory_path, required=True, help='target module path')

parser_build = subparsers.add_parser('build', help='Build functions and packages')
parser_build.set_defaults(func=build_packages)
parser_build.add_argument(
    '-p', '--path', type=directory_path, required=False, default=None,
    help='target module path'
)

parser_report = subparsers.add_parser('report', help='Build functions and packages')
parser_report.set_defaults(func=report_functions)
parser_report.add_argument(
    '-p', '--path', type=directory_path, required=False, default=None,
    help='target module path'
)


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

    registry = Registry()
    config = None
    if args.conf is not None:
        config = ConfigParser.SafeConfigParser()
        config.optionxform = str
        config.read(args.conf)
    return args.func(registry, config, args)
