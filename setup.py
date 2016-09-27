#!/usr/bin/env python
from setuptools import setup

setup(
    name='servant',
    version='0.1',
    py_modules=['servant'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        servant=servant:servant
    ''',
)
