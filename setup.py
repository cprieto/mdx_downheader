# -*- coding: utf-8 -*-

from setuptools import setup
from os import path

HERE = path.abspath(path.dirname(__file__))

setup(
    name='markdown_downheader',
    version = '1.0.0',
    keywords='text filter markdown html headers',
    description='Python markdown extension to downgrade headers',
    long_description='',
    author= 'Cristian Prieto',
    author_email='me@cprieto.com',
    url='http://github.com/cprieto/mdx_downheader',
    py_modules=[],
    install_requires=[],
    license='Simplified BSD License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)