# -*- coding: utf-8 -*-

"""getcrackin.getcrackin: provides entry point main()."""

__version__ = "0.0.1"

import argparse
import sys

def parse_cmdline():

    # Create parser object
    parser = argparse.ArgumentParser(
            description="A CLI app template to get started from, with zero dependencies.")

    # Create mutually exclusive option group for verbosity
    verbose_group = parser.add_mutually_exclusive_group()
    verbose_group.add_argument("-v",
                            "--verbose",
                            action="store_true",
                            default=False,
                            help="More verbose console output",
                            )
    verbose_group.add_argument("-q",
                            "--quiet",
                            action="store_true",
                            default=False,
                            help="Less verbose console output",
                            )

    # Check version of package
    parser.add_argument("--version",
                            action="version",
                            version=__version__,
                            help="Show package version number",
                            )

    # Apply parser and return the namespace object as a dict
    # parsed_object = parser.parse_args()
    # return vars(parsed_object)
    return parser.parse_args()


def main():
    parse_cmdline()

