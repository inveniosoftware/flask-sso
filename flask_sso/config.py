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
Configuration
=============

SSO_ATTRIBUTE_MAP
-----------------

A dictionary mapping HTTP headers to a tuple. The tuple contains whether the
attribute is required and then the name of the attribute.

Example::

# CERN Single-Sign-On
SSO_ATTRIBUTE_MAP = {
    "ADFS_LOGIN": (True, nickname),
    "ADFS_EMAIL": (True, email),
}

# General Shibboleth
SSO_ATTRIBUTE_MAP = {
    "HTTP_SHIB_IDENTITY_PROVIDER": (True, "idp"),
    "HTTP_SHIB_SHARED_TOKEN": (True, "shared_token"),
    "HTTP_SHIB_CN": (True, "cn"),
    "HTTP_SHIB_MAIL": (True, "email"),
    "HTTP_SHIB_GIVENNAME": (False, "first_name"),
    "HTTP_SHIB_SN": (False, "last_name"),
}

SSO_LOGIN_URL
-------------

Url of login handler. Default: `/login/sso`.

SSO_LOGIN_ENDPOINT
------------------

Name of login handler endpoint to be used in `url_for` function.

Example::

>>> from flask.ext.sso.config import *
>>> url_for(SSO_LOGIN_ENDPOINT)
/login/sso
>>> SSO_LOGIN_URL
/login/sso


Default: `sso_login`.
"""

SSO_ATTRIBUTE_MAP = {}

SSO_LOGIN_URL = '/login/sso'

SSO_LOGIN_ENDPOINT = 'sso_login'
