Ananta
======

(Current version doesn't have all features to deploy at AWS)

AWS Lambda packaging library and tools


Requirements
------------

- Python 2.7
- pip (to run commands)
- boto3 (to run commands)


Usage
-----

0. Install
^^^^^^^^^^

.. code-block:: sh

   $ pip install git+https://github.com/attakei/ananta.git
   $ pip install -e .

1. Decorate to lambda function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from ananta import lamnda_function

   @lamnda_function(FunctionName='my_lambda_func', Role='arn:aws:::your:lambda:exec:role')
   def my_lambda_function(event, context):
       do_it()

2. Build zip package to use for AWS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   $ ananta build
   $ ls -l
   ... package.zip ...

3. Deploy to AWS Lambda
^^^^^^^^^^^^^^^^^^^^^^^

Not implemented