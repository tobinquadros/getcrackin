#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import unittest

class ParserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_version_option(self):
        cmdline = ["./getcrackin-runner.py", "--version"]
        proc = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        actual = proc.communicate()
        print "actual is {}".format(actual[0].rstrip())
        expected = "0.0.1"
        self.assertEqual(actual[0].rstrip(), expected, "Version number doesn't match.")

if __name__ == "__main__":
    unittest.main()
