# -*- coding:utf8 -*-
# It is a test root.
import os
import tests as root

current_dir = root.current_dir
"""directory to run test"""

test_dir = os.path.abspath(os.path.dirname(__file__))
"""directory of it"""

samples_dir = root.samples_dir
"""directory of samples"""

working_directory = root.working_directory
