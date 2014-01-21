# -*- coding: utf-8 -*-
##
## This file is part of Flask-SSO
## Copyright (C) 2014 CERN.
##
## Flask-SSO is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Flask-SSO is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Flask-SSO; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

"""
Flask extension
===============

Flask-SSO is initialized like this:

>>> from flask import Flask
>>> from flask_sso import SSO
>>> app = Flask('myapp')
>>> ext = SSO(app=app)
"""

from __future__ import absolute_import

from . import config

from flask import current_app, request
from flask.signals import Namespace


class SSOAttributeError(Exception):
    pass

# Signals
_signals = Namespace()

#: Sent when a user is logged in. In addition to the app (which is the
#: sender), it is passed `user`, which is the user being logged in.
sso_logged_in = _signals.signal('sso-logged-in')


class SSO(object):
    """
    Flask extension

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
    def __init__(self, app=None):
        self.login_callback = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initialize a Flask application.
        """
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
        """
        This will set the callback for the `login` method. It takes one
        argument with attributes map, and should return a Flask response.

        :param callback: The callback for login.
        :type callback: function
        """
        self.login_callback = callback

    def login(self):
        attrs, error = self.parse_attributes()
        if error:
            raise SSOAttributeError

        sso_logged_in.send(current_app._get_current_object(), attributes=attrs)

        if self.login_callback:
            return self.login_callback(attrs)

    def parse_attributes(self):
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

# Version information
from .version import __version__

__all__ = [
    'SSO', '__version__'
]
