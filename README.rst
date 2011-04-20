System session booking forms for COS
====================================

A taste of how Django may be used to help our friends down there.

Sample initial data is supplied in :file:`src/sbb/fictures/initial_data.json`.
Four users have been registered into the system:

    * User ``kelly`` (password: ``kelly``): A regular user. She may not
      request system sessions.

    * User ``kass`` (password: ``kass``): An analyst. She may request
      system session, but may not approve them.

    * User ``petra`` (password: ``petra``): From Calldesk. She may
      approve system sessions.

    * User ``admin`` (password: ``admin``): A Django superuser.


Bootstrapping from a fresh Git checkout
---------------------------------------

This application follows Jacob Kaplan-Moss' `Developing Django apps with
zc.buildout`_.

You need first to generate the `zc.buildout`_ stuff::

    $ python ./bootstrap.py
    Downloading http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg
    Creating directory '/home/carlos/src/system-session-bookings/bin'.
    Creating directory '/home/carlos/src/system-session-bookings/parts'.
    Creating directory '/home/carlos/src/system-session-bookings/eggs'.
    Creating directory '/home/carlos/src/system-session-bookings/develop-eggs'.
    Generated script '/home/carlos/src/system-session-bookings/bin/buildout'.
    $

Then run `zc.buildout`_ itself to fetch Django and create the
environment::

    $ ./bin/buildout 
    Develop: '/home/carlos/src/system-session-bookings/.'
    Getting distribution for 'zc.recipe.egg'.
    Got zc.recipe.egg 1.3.2.
    Getting distribution for 'djangorecipe'.
    Got djangorecipe 0.22.
    Installing python.
    Generated interpreter '/home/carlos/src/system-session-bookings/bin/python'.
    Installing django.
    django: Downloading Django from: http://www.djangoproject.com/download/1.3/tarball/
    Generated script '/home/carlos/src/system-session-bookings/bin/django'.
    Generated script '/home/carlos/src/system-session-bookings/bin/test'.
    $

Now you may create a fresh local database using the usual Django admin
command::

    $ ./bin/django syncdb --noinput
    Creating tables ...
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_user_permissions
    Creating table auth_user_groups
    Creating table auth_user
    Creating table auth_message
    Creating table django_content_type
    Creating table django_session
    Creating table django_admin_log
    Creating table ssb_systemsession
    Installing custom SQL ...
    Installing indexes ...
    Installed 22 object(s) from 1 fixture(s)
    $

At this point the application can be started in the usual way::

    $ ./bin/django runserver
    Validating models...

    0 errors found
    Django version 1.3, using settings 'ssb.testsettings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


.. _zc.buildout: http://buildout.org/
.. _Developing Django apps with zc.buildout: http://jacobian.org/writing/django-apps-with-buildout/
