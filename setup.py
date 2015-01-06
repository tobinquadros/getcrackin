# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""

import os
from setuptools import setup, find_packages

# Utility function to read the DESCRIPTION.rst file, used for long_description.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    author = "Tobin Quadros",
    author_email = "tobinquadros@gmail.com",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities",
    ],
    description = ("CLI app that helps figure out what to get crackin' on next."),
    download_url = "http://github.com/tobinquadros/getcrackin",
    entry_points = {
        "console_scripts": ["getcrackin = getcrackin.getcrackin:main"],
        },
    install_requires = [],
    keywords = "development github issues",
    license = "MIT",
    long_description = read('doc/DESCRIPTION.rst'),
    name = "getcrackin",
    packages = find_packages(exclude = ["tests"]),
    test_suite = "tests",
    url = "http://pypi.python.org/pypi/getcrackin",
    version = "0.0.1"
)

