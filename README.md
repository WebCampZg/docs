WebCamp Docs
============

This repo contains the sources for http://docs.webcampzg.org/

Building
--------

Install prerequisites (preferably into a
[virtual environment](https://virtualenv.pypa.io/en/stable/)):

```
pip install -r requirements.txt
```

Build HTML:

```
make html
```

The docs will be rendered in `_build/html`.

Continuous deployment
---------------------

Any changes pushed to the master branch will be automatically deployed to
[docs.webcampzg.org](http://docs.webcampzg.org/).

On push, a webhook will trigger a build on
[builds.sr.ht](https://builds.sr.ht/). The build manifest can be found in
[`.build.yml`](.build.yml).

The build task checks out this project, renders the HTML and updates the sources
in https://github.com/WebCampZg/webcampzg.github.io/ from where the site is
served, via [Gihub Pages](https://pages.github.com/).

Past builds can be found [here](https://builds.sr.ht/~ihabunek/docs).
