#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import unittest

def shell_out(cmdline):
    """Enable command line testing from the module's runner."""
    proc = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.communicate()[0].rstrip().decode()
    print("actual is {}".format(output))
    return output

class ParserTestCase(unittest.TestCase):
    """Tests for the command line parser."""

    def setUp(self):
        pass

    def tearDown(self):
        try:
            pass
        except:
            pass

    def test_no_options(self):
        """Smoke test for getcrackin-runner.py."""
        cmdline = ["./getcrackin-runner.py"]
        actual = shell_out(cmdline)
        expected = ""
        self.assertEqual(actual, expected, "Should have default output.")

    def test_version_option(self):
        """Display correct version number."""
        cmdline = ["./getcrackin-runner.py", "--version"]
        actual = shell_out(cmdline)
        expected = "0.0.1"
        self.assertEqual(actual, expected, "Version number doesn't match.")

if __name__ == "__main__":
    # Locate and execute all TestCase subclasses.
    unittest.main()

