# -*- coding: utf-8 -*-
#
# This file is part of Flask-SSO
# Copyright (C) 2014, 2015 CERN.
#
# Flask-SSO is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

from unittest import TestCase
from flask import Flask


class FlaskTestCase(TestCase):
    """
    Mix-in class for creating the Flask application
    """

    def setUp(self):
        app = Flask(__name__)
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.logger.disabled = True
        self.app = app
