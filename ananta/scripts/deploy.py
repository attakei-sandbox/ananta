# -*- coding:utf8 -*-
"""Deploy build package
"""
from __future__ import unicode_literals


def deploy_functions(registry, config, args):
    from ananta.scripts.build import build_packages
    from ananta.scripts.upload import upload_functions
    result = build_packages(registry, config, args)
    args.path = result
    upload_functions(registry, config, args)