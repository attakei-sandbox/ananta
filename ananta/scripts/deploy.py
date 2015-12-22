# -*- coding:utf8 -*-
"""Deploy build package
"""
from __future__ import unicode_literals
import zipfile
import json


__author__ = 'attakei'


def deploy_functions(registry, config, args):
    import boto3

    client = boto3.client('lambda')
    functions_list = []
    with zipfile.ZipFile(args.path) as zfp:
        functions_list = json.loads(zfp.read('functions.json'))
    with open(args.path, 'rb') as fp:
        functions_code = fp.read()
    for function_info in functions_list:
        if 'MemorySize' in function_info:
            function_info['MemorySize'] = int(function_info['MemorySize'])
        if 'Timeout' in function_info:
            function_info['Timeout'] = int(function_info['Timeout'])
        function_info['Runtime'] = 'python2.7'
        function_info['Code'] = {'ZipFile': functions_code}
        client.create_function(
            **function_info
        )