Changelog
=========

Here you can see the full list of changes between each Flask-SSO
release.

Version 0.4.0 (released 2015-10-05)

- Login error handler can be added to SSO and will be called with
  required attributes are missing. If login error callback is set
  no `SSOAttributeError` will be raised and application can
  return custom error response based on missing attributes.

Version 0.3.0 (released 2015-07-30)

- The Flask-SSO extension is now released under more permissive
  Revised BSD License. (#6)
- For testing execute run-tests.sh instead of sourcing it. (#4)
- New minimal application example. (#8)
- New Tox support for Python-3.4. (#4)

Version 0.2.0 (released 2014-06-26)

- Allowing ';' separator in HTTP data.
- Fix for dictionary key order in tests.
- Fix for Python 3.3 string comparison.
- New dependency: Blinker.
- Code coverage improved to 100%.
- New configuration option SSO_LOGIN_ENDPOINT.

Version 0.1

- Initial public release.
