========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-cleanlog/badge/?style=flat
    :target: https://readthedocs.org/projects/python-cleanlog
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/cleanlog.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/cleanlog

.. |commits-since| image:: https://img.shields.io/github/commits-since/dohlee/python-cleanlog/v0.1.5.svg
    :alt: Commits since latest release
    :target: https://github.com/dohlee/python-cleanlog/compare/v0.1.5...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/cleanlog.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/cleanlog

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cleanlog.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/cleanlog

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cleanlog.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/cleanlog


.. end-badges

Python package for nice colored logs.

* Free software: MIT license

Installation
============

::

    pip install cleanlog

Documentation
=============

https://python-cleanlog.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
