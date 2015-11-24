# -*- coding:utf8 -*-
"""Ananta : AWS Lambda packager
"""
import sys


__version__ = '0.0.1'


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
