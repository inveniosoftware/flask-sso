===========
 Flask-SSO
===========
.. currentmodule:: flask_sso


.. raw:: html

    <p style="height:22px; margin:0 0 0 2em; float:right">
        <a href="https://travis-ci.org/inveniosoftware/flask-sso">
            <img src="https://travis-ci.org/inveniosoftware/flask-sso.png?branch=master"
                 alt="travis-ci badge"/>
        </a>
        <a href="https://coveralls.io/r/inveniosoftware/flask-sso">
            <img src="https://coveralls.io/repos/inveniosoftware/flask-sso/badge.png?branch=master"
                 alt="coveralls.io badge"/>
        </a>
    </p>


Flask-SSO is a Flask extension permitting to set up Shibboleth
Single-Sign-On authentication in Flask based web applications.

Contents
--------

.. contents::
   :local:
   :backlinks: none


Installation
============

Flask-SSO is on PyPI so all you need is :

.. code-block:: console

    $ pip install flask-sso

The development version can be downloaded from `its page at GitHub
<http://github.com/inveniosoftware/flask-sso>`_.

.. code-block:: console

    $ git clone https://github.com/inveniosoftware/flask-sso.git
    $ cd flask-sso
    $ python setup.py develop
    $ ./run-tests.sh

Requirements
^^^^^^^^^^^^

Flask-SSO has the following dependencies:

* `Flask <https://pypi.python.org/pypi/Flask>`_
* `blinker <https://pypi.python.org/pypi/blinker>`_
* `six <https://pypi.python.org/pypi/six>`_

Flask-SSO requires Python version 2.6, 2.7 or 3.3+


Quickstart
==========

This part of the documentation will show you how to get started in using
Flask-SSO with Flask.

This guide assumes you have successfully installed Flask-SSO and a working
understanding of Flask. If not, follow the installation steps and read about
Flask at http://flask.pocoo.org/docs/.


A Minimal Example
^^^^^^^^^^^^^^^^^

A minimal Flask-SSO usage example looks like this.

First, let's create the application and initialise the extension:

.. code-block:: python

    from flask import Flask, session, redirect
    from flask_sso import SSO
    app = Flask("myapp")
    ext = SSO(app=app)


Second, let's configure the attribute map for converting environment
variables to a dictionary containing user information:

.. code-block:: python

    #: Default attribute map
    SSO_ATTRIBUTE_MAP = {
        'ADFS_AUTHLEVEL': (False, 'authlevel'),
        'ADFS_GROUP': (True, 'group'),
        'ADFS_LOGIN': (True, 'nickname'),
        'ADFS_ROLE': (False, 'role'),
        'ADFS_EMAIL': (True, 'email'),
        'ADFS_IDENTITYCLASS': (False, 'external'),
        'HTTP_SHIB_AUTHENTICATION_METHOD': (False, 'authmethod'),
    }

    app.config.setdefault('SSO_ATTRIBUTE_MAP', SSO_ATTRIBUTE_MAP)


Third, let's set up a login handler function that reads user information
and stores it for later usage:

.. code-block:: python

    @sso.login_handler
    def login_callback(user_info):
        """Store information in session."""
        session["user"] = user_info


Fourth, we can now greet the user using his SSO login name:

.. code-block:: python

    @app.route("/")
    def index():
        """Display user information or force login."""
        if "user" in session:
            return "Welcome {name}".format(name=session["user"]["nickname"])
        return redirect(app.config["SSO_LOGIN_URL"])


Configuration
=============

.. automodule:: flask_sso.config


API
===

This documentation section is automatically generated from Flask-SSO's
source code.

Flask-SSO
^^^^^^^^^

.. automodule:: flask_sso

.. autoclass:: SSO
   :members:


.. include:: ../CHANGES

.. include:: ../CONTRIBUTING.rst


License
=======

.. include:: ../LICENSE

.. include:: ../AUTHORS
