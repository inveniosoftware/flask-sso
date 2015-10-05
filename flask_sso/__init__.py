# -*- coding: utf-8 -*-
#
# This file is part of Flask-SSO
# Copyright (C) 2014, 2015 CERN.
#
# Flask-SSO is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""
Implement Shibboleth Single-Sign-On authentication.

Flask-SSO is initialized like this:

Initialization of the extension:

>>> from flask import Flask
>>> from flask_sso import SSO
>>> app = Flask('myapp')
>>> ext = SSO(app=app)

or alternatively using the factory pattern:

>>> app = Flask('myapp')
>>> ext = SSO()
>>> ext.init_app(app)
"""

from __future__ import absolute_import

from . import config

from flask import current_app, request
from flask.signals import Namespace

from .version import __version__


class SSOAttributeError(Exception):

    """General SSO Attribute error."""

# Signals
_signals = Namespace()

#: Sent when a user is logged in. In addition to the app (which is the
#: sender), it is passed `user`, which is the user being logged in.
sso_logged_in = _signals.signal('sso-logged-in')


class SSO(object):

    """Flask extension implementation."""

    def __init__(self, app=None):
        """Initialize login callback."""
        self.login_callback = None
        self.login_error_callback = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize a Flask application."""
        self.app = app
        # Follow the Flask guidelines on usage of app.extensions
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        if 'sso' in app.extensions:
            raise RuntimeError("Flask application already initialized")
        app.extensions['sso'] = self

        # Set default configuration
        app.config.setdefault('SSO_LOGIN_URL', config.SSO_LOGIN_URL)
        app.config.setdefault('SSO_LOGIN_ENDPOINT', config.SSO_LOGIN_ENDPOINT)
        app.config.setdefault('SSO_ATTRIBUTE_MAP', config.SSO_ATTRIBUTE_MAP)

        app.add_url_rule(app.config.get('SSO_LOGIN_URL'),
                         app.config.get('SSO_LOGIN_ENDPOINT'),
                         self.login)

    def login_handler(self, callback):
        """Set the callback for the `login` method.

        It takes one argument with attributes map, and should return a Flask
        response.

        :param callback: The callback for login.
        :type callback: function
        """
        self.login_callback = callback

    def login_error_handler(self, callback):
        """Set the error callback for `login` method.

        It takes one argument with attributes map, and should return a Flask
        response.

        :param callback: The callback for login error.
        :type callback: function
        """
        self.login_error_callback = callback

    def login(self):
        """Implement application login endpoint for SSO."""
        attrs, error = self.parse_attributes()
        if error:
            if self.login_error_callback:
                return self.login_error_callback(attrs)
            else:
                raise SSOAttributeError

        sso_logged_in.send(current_app._get_current_object(), attributes=attrs)

        if self.login_callback:
            return self.login_callback(attrs)

    def parse_attributes(self):
        """Parse arguments from environment variables."""
        attrs = {}
        error = False
        for header, attr in self.app.config['SSO_ATTRIBUTE_MAP'].items():
            required, name = attr
            value = request.environ.get(header, None)

            attrs[name] = value
            if not value or value == '':
                if required:
                    error = True
        return attrs, error


__all__ = ('SSO', '__version__')
