# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, 'Readme.rst')) as f:
    long_description = f.read()

setup(
    name='markdown_downheader',
    version = '1.1.1',
    keywords='text filter markdown html headers',
    description=long_description,
    long_description='Python Markdown extension to downgrade headers, for example, from h1 to h2',
    author= 'Cristian Prieto',
    author_email='me@cprieto.com',
    url='http://github.com/cprieto/mdx_downheader',
    py_modules=['mdx_downheader'],
    install_requires=['Markdown'],
    license='Simplified BSD License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
