#!/bin/sh
# SPDX-FileCopyrightText: 2014, 2016 CERN.
# SPDX-License-Identifier: BSD-3-Clause

pydocstyle flask_sso tests && \
isort -rc -c -df **/*.py && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test && \
sphinx-build -qnNW -b doctest docs docs/_build/doctest
