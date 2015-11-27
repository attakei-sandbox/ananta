# -*- coding:utf8 -*-
# It is a test root.
import os
import contextlib


current_dir = os.path.abspath(os.getcwd())
"""directory to run test"""

test_dir = os.path.abspath(os.path.dirname(__file__))
"""directory of it"""

samples_dir = os.path.join(test_dir, 'samples')
"""directory of samples"""


# http://code.activestate.com/recipes/576620-changedirectory-context-manager/
#
@contextlib.contextmanager
def working_directory(path):
    """A context manager which changes the working directory to the given
    path, and then changes it back to its previous value on exit.

    """
    prev_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)
