===========
 Flask-SSO
===========

.. image:: https://travis-ci.org/inveniosoftware/flask-sso.png?branch=master
    :target: https://travis-ci.org/inveniosoftware/flask-sso
.. image:: https://coveralls.io/repos/inveniosoftware/flask-sso/badge.png?branch=master
    :target: https://coveralls.io/r/inveniosoftware/flask-sso
.. image:: https://pypip.in/v/Flask-SSO/badge.png
   :target: https://pypi.python.org/pypi/Flask-SSO/
.. image:: https://pypip.in/d/Flask-SSO/badge.png
   :target: https://pypi.python.org/pypi/Flask-SSO/

About
=====
Flask-SSO is a Flask extension permitting to set up Shibboleth
Single-Sign-On authentication in Flask based web applications.

Installation
============
Flask-SSO is on PyPI so all you need is: ::

    pip install Flask-SSO

Documentation
=============
Documentation is readable at http://flask-sso.readthedocs.org or can be built using Sphinx: ::

    git submodule init
    git submodule update
    pip install Sphinx
    python setup.py build_sphinx

Testing
=======
Running the test suite is as simple as: ::

    python setup.py test

or, to also show code coverage: ::

    ./run-tests.sh
