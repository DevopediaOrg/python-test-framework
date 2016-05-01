#!/usr/bin/env python
# encoding: utf-8
"""
Read and manage configuration.
 
=======================================================================
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
=======================================================================
"""


import argparse
from datetime import datetime
import getpass
import json
import os
import sys
import unittest

from tests import *


class SysConfig:
    def __init__(self):
        self.params = None

    def read_json(self, file):
        """Read configuration from a JSON file."""

        try:
            with open(file, 'r') as f:
                self.params = json.load(f)
        except OSError as err:
            print("Config file not found: {0}".format(err))
        except ValueError as err:
            print("Bad syntax in JSON input: {0}".format(err))  
        else:
            # No exceptions
            return
        
        # Exit if encountered an exception
        exit()


class TestConfig:
    def __init__(self):
        self.init_context()
        self.parse_args()

    def init_context(self):
        """Initialize context for this execution."""
        self.username = getpass.getuser()
        self.startts = datetime.now()
        self.path = os.path.normpath(os.path.dirname(__file__)+'/..')
        self.command = " ".join(sys.argv)

    def parse_args(self):
        """Parse command line arguments."""

        parser = argparse.ArgumentParser(description='Test automation framework.')
        parser.add_argument('-i', '--in', help='Input file containing all test cases.', required=False)
        args = vars(parser.parse_args())

        if args['in']:
            with open(args['in'], 'r') as f:
                self.testcases = [l.strip() for l in f if '.' in l]
        else:
            self.testcases = []
        self.__init_testsuite()

    def __init_testsuite(self):
        """Make a list of test cases to execute."""
        
        self.testsuite = unittest.TestSuite()

        for tc in self.testcases:
            try:
                mod_name, func_name = tc.rsplit('.', 1)
                func = getattr(eval(mod_name), func_name)
                self.testsuite.addTest(unittest.makeSuite(func))
            except NameError as err:
                print("Module not found: {0}".format(err))
            except AttributeError as err:
                print("Test case class not found: {0}".format(err))  
               
        
        # Discover tests if nothing is given explicitly
        if not self.testsuite.countTestCases():
            loader = unittest.TestLoader()
            self.testsuite = loader.discover(start_dir=os.path.dirname(__file__)+"/..", pattern="tc_*.py") 

