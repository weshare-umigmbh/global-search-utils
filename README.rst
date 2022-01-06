Python utility library for GlobalSearch
=======================================

`GlobalSearch utils` includes utility functions for that are used by several ingest endpoints of GlobalSearch


Quick Start
-----------

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 3.9


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install -e git+ssh://git@github.com/weshare-umigmbh/global-search-utils.git#egg=globalsearch-utils


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install -e git+ssh://git@github.com/weshare-umigmbh/global-search-utils.git#egg=globalsearch-utils

Try out Git Bash if you're experiencing problems like ``git@github.com: Permission denied (publickey)``.


Install modules from feature branches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    pip install -e git+ssh://git@github.com/weshare-umigmbh/global-search-utils.git@<your-branch>#egg=globalsearch-utils


Example Usage
~~~~~~~~~~~~~

.. code:: python

    from globalsearch.utils.elastic_client import get_elastic_client
    client = get_elastic_client()
