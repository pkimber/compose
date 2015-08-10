Compose
*******

Django application containing a couple of models for use with the block app
when building a simple CMS site.

Install
=======

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-compose
  source venv-compose/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  ./init_dev.sh

Release
=======

https://www.pkimber.net/open/
