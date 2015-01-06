#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import unittest

def shell_out(cmdline):
    proc = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.communicate()[0].rstrip()
    print "actual is {}".format(output)
    return output

class ParserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_no_options(self):
        cmdline = ["./getcrackin-runner.py"]
        actual = shell_out(cmdline)
        expected = ""
        self.assertEqual(actual, expected, "Should have default output.")

    def test_version_option(self):
        cmdline = ["./getcrackin-runner.py", "--version"]
        actual = shell_out(cmdline)
        expected = "0.0.1"
        self.assertEqual(actual, expected, "Version number doesn't match.")

if __name__ == "__main__":
    unittest.main()
