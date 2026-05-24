# SPDX-FileCopyrightText: 2014, 2016 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""Default Flask test case."""

from unittest import TestCase

from flask import Flask


class FlaskTestCase(TestCase):
    """Mix-in class for creating the Flask application."""

    def setUp(self):
        """Set up the test case."""
        app = Flask(__name__)
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.logger.disabled = True
        self.app = app
