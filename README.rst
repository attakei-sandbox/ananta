Ananta
======

AWS Lambda packaging library and tools


Requirements
------------

- Python 2.7
- boto3 (to run commands)


Usage
-----

0. Install
^^^^^^^^^^

.. code-block:: sh

   $ pip install git+https://github.com/attakei/Ananta.git
   $ pip install -e .

1. Decorate to lambda function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from ananta import lambda_config

   @lambda_config(name='my_lambda_func', role='arn:aws:::your:lambda:exec:role')
   def my_lambda_function(event, context):
       do_it()

2. Dump
^^^^^^^

.. code-block:: bash

   $ ananta dump -p yourproject
   [{"name":"my_lambda_func", "handler":"yourproject.my_lambda_function"}]

