#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name = "PyV8",
    version = "0.8",
    author = "desertkun",
    license = "",
    url = "https://github.com/desertkun/PyV8-linux64",
    packages=find_packages(),
    zip_safe = False,
    package_data = {
        'pyv8': ['*.so'],
    },
    classifiers = [
        "Development Status :: 0.8",
        "Environment :: Server",
        "Intended Audience :: Developers",
        "License :: All rights reserved",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ]
)
