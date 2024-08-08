python-relattrs
===============

`relattrs` is a small utility library for recursively getting, setting, checking, and deleting attributes of an object using a dotted string representation. This can be particularly useful when dealing with nested objects.

Installation
------------

You can install `relattrs` via pip:

.. code-block:: bash

    pip install relattrs

Functions
---------

The library provides four main functions:

- `rgetattr`: Recursively gets an attribute from an object.
- `rhasattr`: Recursively checks if an attribute exists on an object.
- `rsetattr`: Recursively sets an attribute on an object.
- `rdelattr`: Recursively deletes an attribute from an object.

Usage
-----

Here's how you can use each function:

### rgetattr

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

**Example with `sep` parameter:**

.. code-block:: python

    from relattrs import rgetattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    print(rgetattr(obj, "B|C|value", sep="|"))  # Output: 1

### rhasattr

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

**Example with `sep` parameter:**

.. code-block:: python

    from relattrs import rhasattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    print(rhasattr(obj, "B|C|value", sep="|"))  # Output: True
    print(rhasattr(obj, "B|C|val", sep="|"))    # Output: False

### rsetattr

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

**Example with `sep` parameter:**

.. code-block:: python

    from relattrs import rsetattr

    class A:
        class B:
            class C:
                value = 1

    obj = A()
    rsetattr(obj, "B|C|value", 2, sep="|")
    print(obj.B.C.value)  # Output: 2

### rdelattr

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

**Example with `sep` parameter:**

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
-------

This project is licensed under the MIT License.
