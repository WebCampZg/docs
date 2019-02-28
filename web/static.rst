===============
Static websites
===============

To avoid having one Django app running per year, and all complications which
come with it, websites of previous years are crawled to make a static copy and
the static files are served. Only the current year is served by a Django app.

Example of a static website:

* Web: https://2018.webcampzg.org/
* Sources: https://github.com/WebCampZg/2018.static

Freeze
------

In the conference-web project, remove parts of the website which should not be
present in the static website - typically the login links/forms and the
dashboard. For example check out `this commit`_.

Crawl a living Django website to make a static copy.

.. code-block:: sh

    wget --page-requisites --mirror 2018.webcampzg.org

Create a repo named `<year>.static`_ and push the static site contents there.

Deploy
------

How to deploy a static site, such as https://github.com/WebCampZg/2018.static.

Clone the website:

.. code-block:: sh

    git clone https://github.com/WebCampZg/2018.static.git ~/web/2018.static

Configure nginx to serve it:

.. code-block:: nginx
   :caption: ``/etc/nginx/sites-available/2018.webcampzg.org``

    server {
      listen 80;
      server_name 2018.webcampzg.org;

      return 301 https://$server_name$request_uri;
    }

    server {
      listen 443;
      server_name 2018.webcampzg.org;
      add_header X-Clacks-Overhead "GNU Terry Pratchett";

      access_log /var/log/nginx/2018.webcampzg.org-access.log;
      error_log /var/log/nginx/2018.webcampzg.org-error.log;

      ssl on;
      ssl_certificate     /etc/letsencrypt/live/webcampzg.org/fullchain.pem;
      ssl_certificate_key /etc/letsencrypt/live/webcampzg.org/privkey.pem;

      location / {
        root /home/webcamp/web/2018.static/;
      }
    }

Reload nginx:

.. code-block:: sh

    sudo service nginx reload

The static website should now be available at https://2018.webcampzg.org/
