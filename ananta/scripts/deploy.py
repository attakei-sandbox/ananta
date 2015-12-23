# -*- coding:utf8 -*-
"""Deploy build package
"""
from __future__ import unicode_literals
import zipfile
import json
import logging


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
        logging.info(function_info['FunctionName'])
        if 'MemorySize' in function_info:
            function_info['MemorySize'] = int(function_info['MemorySize'])
        if 'Timeout' in function_info:
            function_info['Timeout'] = int(function_info['Timeout'])
        set_function(client, function_info, functions_code)


def set_function(client, info, code):
    from botocore.exceptions import ClientError
    try:
        client.update_function_code(
            FunctionName=info['FunctionName'],
            ZipFile=code,
        )
    except ClientError as err:
        if 'ResourceNotFoundException' not in err.message:
            raise err
        client.create_function(
            Runtime='python2.7',
            Code={'ZipFile': code},
            **info
        )
