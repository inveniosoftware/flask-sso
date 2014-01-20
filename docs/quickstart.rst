.. _quickstart:

Quickstart
==========

This guide assumes you have successfully installed Flask-SSO and a working
understanding of Flask. If not, follow the installation steps and read about
Flask at http://flask.pocoo.org/docs/.


A Minimal Example
-----------------

A minimal Flask-SSO usage example looks like this. First create the
application and initialize the extension:

>>> from flask import Flask
>>> from flask_sso import SSO
>>> app = Flask('myapp')
>>> ext = SSO(app=app)

Some Extended Example
---------------------
Flask-SSO also has support for CHANGEME

.. literalinclude:: ../tests/helpers.py
