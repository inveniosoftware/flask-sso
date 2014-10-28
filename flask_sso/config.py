# -*- coding: utf-8 -*-
#
# This file is part of Flask-SSO
# Copyright (C) 2014, 2015 CERN.
#
# Flask-SSO is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""The details of the application settings that can be customized.


SSO_ATTRIBUTE_MAP
-----------------

A dictionary mapping HTTP headers to a tuple. The tuple contains whether the
attribute is required and then the name of the attribute.

Example:

.. code-block:: python

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

Example:

.. code-block:: python

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
