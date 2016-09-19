===========
 Flask-SSO
===========

.. image:: https://img.shields.io/travis/inveniosoftware/flask-sso.svg
        :target: https://travis-ci.org/inveniosoftware/flask-sso

.. image:: https://img.shields.io/coveralls/inveniosoftware/flask-sso.svg
        :target: https://coveralls.io/r/inveniosoftware/flask-sso

.. image:: https://img.shields.io/github/tag/inveniosoftware/flask-sso.svg
        :target: https://github.com/inveniosoftware/flask-sso/releases

.. image:: https://img.shields.io/pypi/dm/flask-sso.svg
        :target: https://pypi.python.org/pypi/flask-sso

.. image:: https://img.shields.io/github/license/inveniosoftware/flask-sso.svg
        :target: https://github.com/inveniosoftware/flask-sso/blob/master/LICENSE

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

    python setup.py build_sphinx

Testing
=======
Running the test suite is as simple as: ::

    python setup.py test

or, to also test documentation and packaging: ::

    ./run-tests.sh
