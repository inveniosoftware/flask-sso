# -*- coding: utf-8 -*-
#
# This file is part of Flask-SSO
# Copyright (C) 2014, 2015 CERN.
#
# Flask-SSO is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

from __future__ import absolute_import

import six

from .helpers import FlaskTestCase

from contextlib import contextmanager
from flask import request_started, request
from flask_sso import SSO, config as default_config, SSOAttributeError


class TestSSO(FlaskTestCase):
    """
    Tests of extension creation
    """
    def test_version(self):
        # Assert that version number can be parsed.
        from flask_sso import __version__
        from distutils.version import LooseVersion
        LooseVersion(__version__)

    def test_creation(self):
        assert 'sso' not in self.app.extensions
        SSO(app=self.app)
        assert isinstance(self.app.extensions['sso'], SSO)

    def test_creation_old_flask(self):
        # Simulate old Flask (pre 0.9)
        del self.app.extensions
        SSO(app=self.app)
        assert isinstance(self.app.extensions['sso'], SSO)

    def test_creation_init(self):
        assert 'sso' not in self.app.extensions
        r = SSO()
        r.init_app(app=self.app)
        assert isinstance(self.app.extensions['sso'], SSO)

    def test_double_creation(self):
        SSO(app=self.app)
        self.assertRaises(RuntimeError, SSO, app=self.app)

    def test_default_config(self):
        SSO(app=self.app)
        for k in dir(default_config):
            if k.startswith('SSO_'):
                assert self.app.config.get(k) == getattr(default_config, k)

    def test_login_handler(self):
        sso = SSO(app=self.app)

        @sso.login_handler
        def _callback(attr):
            return '{0}'.format(attr)

        @contextmanager
        def request_environ_set(app, data):

            def handler(sender, **kwargs):
                for (k, v) in data.items():
                    request.environ[k] = v

            with request_started.connected_to(handler, app):
                yield

        def run(conf, data, expected_data):
            self.app.config['SSO_ATTRIBUTE_MAP'] = conf
            with request_environ_set(self.app, data):
                with self.app.test_client() as c:
                    resp = c.get(self.app.config['SSO_LOGIN_URL'])
                    self.assertEqual(resp.data,
                                     six.b('{0}'.format(expected_data)))

        conf = {'FOO': (True, 'bar'), 'BAZ': (False, 'baa')}
        data = {'FOO': 'foo'}
        expected_data = {'bar': 'foo', 'baa': None}

        run(conf, data, expected_data)

        conf = {'FOO': (True, 'bar'), 'BAZ': (True, 'baa')}
        data = {'FOO': 'foo', 'BAZ': 'baz'}
        expected_data = {'bar': 'foo', 'baa': 'baz'}

        run(conf, data, expected_data)

        conf = {'FOO': (True, 'bar'), 'BAZ': (False, 'baa')}
        data = {'FOO': 'foo', 'BAZ': 6}
        expected_data = {'bar': 'foo', 'baa': 6}

        run(conf, data, expected_data)

    def test_invalid_attribute_map(self):
        SSO(app=self.app)

        @contextmanager
        def request_environ_set(app, data):

            def handler(sender, **kwargs):
                for (k, v) in data.items():
                    request.environ[k] = v

            with request_started.connected_to(handler, app):
                yield

        conf = {'FOO': (True, 'bar'), 'BAZ': (True, 'baa')}
        data = {'FOO': 'foo'}

        self.app.config['SSO_ATTRIBUTE_MAP'] = conf
        with request_environ_set(self.app, data):
            with self.app.test_client() as c:
                try:
                    c.get(self.app.config['SSO_LOGIN_URL'])
                    assert False
                except SSOAttributeError:
                    assert True

    def test_login_error_handler(self):
        sso = SSO(app=self.app)

        @sso.login_handler
        def _callback(attr):
            return '{0}'.format(attr)

        @sso.login_error_handler
        def _callback_error(attr):
            return '{0}'.format(attr)

        @contextmanager
        def request_environ_set(app, data):

            def handler(sender, **kwargs):
                for (k, v) in data.items():
                    request.environ[k] = v

            with request_started.connected_to(handler, app):
                yield

        def run(conf, data, expected_data):
            self.app.config['SSO_ATTRIBUTE_MAP'] = conf
            with request_environ_set(self.app, data):
                with self.app.test_client() as c:
                    resp = c.get(self.app.config['SSO_LOGIN_URL'])
                    self.assertEqual(resp.data,
                                     six.b('{0}'.format(expected_data)))

        conf = {'FOO': (True, 'bar'), 'BAZ': (False, 'baa')}
        data = {'FOO': 'foo'}
        expected_data = {'bar': 'foo', 'baa': None}

        run(conf, data, expected_data)

        conf = {'FOO': (True, 'bar'), 'BAZ': (True, 'baa')}
        data = {'FOO': 'foo', 'BAZ': 'baz'}
        expected_data = {'bar': 'foo', 'baa': 'baz'}

        run(conf, data, expected_data)

        conf = {'FOO': (True, 'bar'), 'BAZ': (False, 'baa')}
        data = {'FOO': 'foo', 'BAZ': 6}
        expected_data = {'bar': 'foo', 'baa': 6}

        run(conf, data, expected_data)

        conf = {'FOO': (True, 'bar'), 'BAZ': (False, 'baa')}
        data = {'FOO': None, 'BAZ': 6}
        expected_data = {'bar': None, 'baa': 6}

        run(conf, data, expected_data)

        # login handler will not be called when required attributes are missing
        @sso.login_handler
        def _callback_(attr):
            assert False

        conf = {'FOO': (True, 'bar'), 'BAZ': (False, 'baa')}
        data = {'FOO': None, 'BAZ': 6}
        expected_data = {'bar': None, 'baa': 6}

        run(conf, data, expected_data)

        # login error handler will not be called when required attributes are
        # present

        @sso.login_handler
        def _callback__(attr):
            return '{0}'.format(attr)

        @sso.login_error_handler
        def _callback_error_(attr):
            assert False

        conf = {'FOO': (True, 'bar'), 'BAZ': (False, 'baa')}
        data = {'FOO': 'foo', 'BAZ': 6}
        expected_data = {'bar': 'foo', 'baa': 6}

        run(conf, data, expected_data)
