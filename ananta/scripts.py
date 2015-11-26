# -*- coding:utf8 -*-
"""Ananta : Console scripts
"""
import sys
import argparse
import json


def dump_functions(args):
    """Scan functions decorated by lambda_config, and dump as json
    """
    print(json.dumps([]))


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')
parser_dump = subparsers.add_parser('dump', help='dump as YAML')
parser_dump.set_defaults(func=dump_functions)


def main(args=None):
    """Console script endpoint

    :param args: console arguments
    :type args: list
    :returns: console return code
    :rtype: int
    """
    if args is None:
        args = sys.argv
    return 0
