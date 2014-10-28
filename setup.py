# -*- coding: utf-8 -*-
#
# This file is part of Flask-SSO
# Copyright (C) 2014, 2015 CERN.
#
# Flask-SSO is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

from setuptools import setup
import os
import re

# Get the version string.  Cannot be done with import!
with open(os.path.join('flask_sso', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='Flask-SSO',
    version=version,
    url='http://github.com/inveniosoftware/flask-sso/',
    license='BSD',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description='Flask-SSO extension that eases Shibboleth authentication.',
    long_description=open('README.rst').read(),
    packages=['flask_sso'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'blinker',
        'six',
    ],
    extras_require={
        'docs': ['sphinx'],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'coverage'],
)
