Tutorial 0: Installation
========================

This short tutorial walks through installing **sqCAD** so you can start using
it in Python scripts or notebooks.

Prerequisites
-------------

- Python 3.9 or newer.
- A virtual environment (recommended), for example created with ``venv`` or ``conda``.

Install from PyPI
-----------------

For most users, installing from PyPI is the simplest option.

.. code-block:: bash

   pip install sqcad

After installation, you can verify that sqCAD imports correctly:

.. code-block:: python

   import sqcad

   print(sqcad.about())

Development install (from source)
---------------------------------

If you want to work on sqCAD itself or track the latest changes from GitHub,
install it in editable (development) mode.

.. code-block:: bash

   git clone https://github.com/elizabethkunz/sqcad.git
   cd sqcad
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[docs]"

This installs sqCAD along with its documentation dependencies, so you can build
the docs locally using:

.. code-block:: bash

   cd docs
   make html

Next steps
----------

Once sqCAD is installed and you have confirmed that ``import sqcad`` works, you
can continue to the :doc:`Quickstart <../quickstart>` for a minimal usage
example, or browse the :doc:`API Reference <../api>` for details on individual
functions and classes.

