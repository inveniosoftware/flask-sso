==================
 Flask-SSO v0.4.0
==================

Flask-SSO v0.4.0 was released on October 5, 2015.

About
-----

Flask-SSO is a Flask extension permitting to set up Shibboleth
Single-Sign-On authentication in Flask based web applications.

What's new
----------

- Login error handler can be added to SSO and will be called with
  required attributes are missing. If login error callback is set
  no `SSOAttributeError` will be raised and application can
  return custom error response based on missing attributes.

Installation
------------

   $ pip install flask-sso==0.4.0

Documentation
-------------

   http://flask-sso.readthedocs.org/en/v0.4.0

Happy hacking and thanks for flying Flask-SSO.

| Invenio Development Team
|   Email: info@invenio-software.org
|   IRC: #invenio on irc.freenode.net
|   Twitter: http://twitter.com/inveniosoftware
|   GitHub: https://github.com/inveniosoftware/flask-sso
|   URL: http://invenio-software.org
