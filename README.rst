.. image:: https://img.shields.io/pypi/pyversions/relattrs
   :target: https://www.python.org/
   :alt: PyPI - Python Version
.. image:: https://img.shields.io/pypi/v/relattrs?color=blue
   :target: https://pypi.org/project/relattrs/
   :alt: PyPI - Version
.. image:: https://results.pre-commit.ci/badge/github/Nibblex/python-relattrs/main.svg
   :target: https://results.pre-commit.ci/latest/github/Nibblex/python-relattrs/main
   :alt: pre-commit.ci status
.. image:: https://codecov.io/gh/Nibblex/python-relattrs/graph/badge.svg?token=JL8M6865RB
   :target: https://codecov.io/gh/Nibblex/python-relattrs
.. image:: https://img.shields.io/pypi/l/relattrs
   :target: https://github.com/Nibblex/python-relattrs/blob/main/LICENSE
   :alt: PyPI - License
.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
   :target: https://github.com/astral-sh/ruff
   :alt: Ruff

python-relattrs
===============

*relattrs* is a small utility library for recursively getting, setting, checking, and deleting attributes of an object using a dotted string representation. This can be particularly useful when dealing with nested objects.

The library provides four main functions:

- *rgetattr*: Recursively gets an attribute from an object.
- *rhasattr*: Recursively checks if an attribute exists on an object.
- *rsetattr*: Recursively sets an attribute on an object.
- *rdelattr*: Recursively deletes an attribute from an object.

Installation
============

You can install *relattrs* via pip:

.. code-block:: bash

    pip install relattrs

Usage
=====

**rgetattr**

Recursively gets an attribute from an object based on a dotted string representation.

**Example:**

.. code-block:: python

    from relattrs import rgetattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    print(rgetattr(obj, "B.C.value"))  # Output: 1

**Example with *sep* parameter:**

.. code-block:: python

    from relattrs import rgetattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    print(rgetattr(obj, "B|C|value", sep="|"))  # Output: 1

**Example with *default* parameter:**

.. code-block:: python

    from relattrs import rgetattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    print(rgetattr(obj, "B.C.val", "Not found"))  # Output: Not found

**rhasattr**

Recursively checks if an object has an attribute based on a dotted string representation.

**Example:**

.. code-block:: python

    from relattrs import rhasattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    print(rhasattr(obj, "B.C.value"))  # Output: True
    print(rhasattr(obj, "B.C.val"))    # Output: False

**Example with *sep* parameter:**

.. code-block:: python

    from relattrs import rhasattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    print(rhasattr(obj, "B|C|value", sep="|"))  # Output: True
    print(rhasattr(obj, "B|C|val", sep="|"))    # Output: False

**rsetattr**

Recursively sets an attribute on an object based on a dotted string representation.

**Example:**

.. code-block:: python

    from relattrs import rsetattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    rsetattr(obj, "B.C.value", 2)
    print(obj.B.C.value)  # Output: 2

**Example with *sep* parameter:**

.. code-block:: python

    from relattrs import rsetattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    rsetattr(obj, "B|C|value", 2, sep="|")
    print(obj.B.C.value)  # Output: 2

**rdelattr**

Recursively deletes an attribute from an object based on a dotted string representation.

**Example:**

.. code-block:: python

    from relattrs import rdelattr, rhasattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    rdelattr(obj, "B.C.value")
    print(rhasattr(obj, "B.C.value"))  # Output: False

**Example with *sep* parameter:**

.. code-block:: python

    from relattrs import rdelattr, rhasattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    rdelattr(obj, "B|C|value", sep="|")
    print(rhasattr(obj, "B|C|value", sep="|"))  # Output: False

License
=======

This project is licensed under the MIT License.
