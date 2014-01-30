#!/usr/bin/env python

import sys
from setuptools import setup

import os

os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

version = "1.0.32"

config = dict(
    name = 'pydot2',
    version = version,
    description = 'Python interface to Graphviz\'s Dot',
    author = 'Ero Carrera',
    author_email = 'ero@dkbza.org',
    url = 'http://code.google.com/p/pydot/',
    download_url = 'http://pydot.googlecode.com/files/pydot-%s.tar.gz' % version,
    license = 'MIT',
    keywords = 'graphviz dot graphs visualization',
    platforms = ['any'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    py_modules = ['pydot', 'dot_parser'],
    install_requires = ['pyparsing', 'setuptools'],
    data_files = [('.', ['LICENSE', 'README'])])


if sys.version_info >= (3,):
    config.update(dict(
        use_2to3=True,
    ))

setup(**config)
