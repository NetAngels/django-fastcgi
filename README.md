Description
-----------

Package for deploying django projects via FastCGI for django version 1.9 or higher.

Django deploy method via FastCGI for shared-hosting described [here](https://docs.djangoproject.com/en/1.8/howto/deployment/fastcgi/#running-django-on-a-shared-hosting-provider-with-apache)

Examples
--------

### Example of myproject.fcgi file

    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    import os
    import sys

    # Add a custom Python path.
    sys.path.insert(0, "/path/to/project/myproject")

    # Switch to the directory of your project. (Optional.)
    os.chdir("/path/to/project/myproject")

    # Set the DJANGO_SETTINGS_MODULE environment variable.
    os.environ['DJANGO_SETTINGS_MODULE'] = "myproject.settings"

    from django_fastcgi.servers.fastcgi import runfastcgi
    from django.core.servers.basehttp import get_internal_wsgi_application

    wsgi_application = get_internal_wsgi_application()
    runfastcgi(wsgi_application, method="prefork", daemonize="false", minspare=1, maxspare=1, maxchildren=1)
