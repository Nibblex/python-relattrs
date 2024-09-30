from functools import reduce
from typing import Any, Optional


def rgetattr(obj: object, rattr: str, *default, sep: Optional[str] = None) -> Any:
    """
    Recursively gets an attribute from an object based on a dotted string representation.

    Args:
        obj: The object from which to retrieve the attribute.
        rattr: The dotted string representation of the attribute to retrieve.
        default: The default value to return if the attribute does not exist.
        sep: The separator used to split the string representation. Defaults to '.' (dot).

    Returns:
        Any: The value of the attribute.

    Raises:
        AttributeError: If the attribute does not exist and no default value is provided.

    Example:
        >>> from relattrs import rgetattr
        >>> class A:
        ...     class B:
        ...         class C:
        ...             value = 1
        >>> obj = A()
        >>> rgetattr(obj, "B.C.value")
        1
    """

    rattr = rattr.split(sep or ".")
    if len(default) == 1:
        try:
            return reduce(getattr, rattr, obj)
        except AttributeError:
            return default[0]

    return reduce(getattr, rattr, obj)


def rhasattr(obj: object, rattr: str, sep: Optional[str] = None) -> bool:
    """
    Recursively checks if an object has an attribute based on a dotted string representation.

    Args:
        obj: The object to check.
        rattr: The dotted string representation of the attribute to check.
        sep: The separator used to split the string representation. Defaults to '.' (dot).

    Returns:
        bool: True if the attribute exists, False otherwise.

    Example:
        >>> from relattrs import rhasattr
        >>> class A:
        ...     class B:
        ...         class C:
        ...             value = 1
        >>> obj = A()
        >>> rhasattr(obj, "B.C.value")
        True
        >>> rhasattr(obj, "B.C.val")
        False
    """

    rattr = rattr.split(sep or ".")
    obj = reduce(getattr, rattr[:-1], obj)
    return hasattr(obj, rattr[-1])


def rsetattr(obj: object, rattr: str, val: Any, sep: Optional[str] = None) -> None:
    """
    Recursively sets an attribute on an object based on a dotted string representation.

    Args:
        obj: The object on which to set the attribute.
        rattr: The dotted string representation of the attribute to set.
        val: The value to set.
        sep: The separator used to split the string representation. Defaults to '.' (dot).

    Example:
        >>> from relattrs import rsetattr
        >>> class A:
        ...     class B:
        ...         class C:
        ...             value = 1
        >>> obj = A()
        >>> rsetattr(obj, "B.C.value", 2)
        >>> obj.B.C.value
        2
    """

    rattr = rattr.split(sep or ".")
    obj = reduce(getattr, rattr[:-1], obj)
    setattr(obj, rattr[-1], val)


def rdelattr(obj: object, rattr: str, sep: Optional[str] = None) -> None:
    """
    Recursively deletes an attribute from an object based on a dotted string representation.

    Args:
        obj: The object from which to delete the attribute.
        rattr: The dotted string representation of the attribute to delete.
        sep: The separator used to split the string representation. Defaults to '.' (dot).

    Example:
        >>> from relattrs import rdelattr
        >>> class A:
        ...     class B:
        ...         class C:
        ...             value = 1
        >>> obj = A()
        >>> rdelattr(obj, "B.C.value")
        >>> rhasattr(obj, "B.C.value")
        False
    """

    rattr = rattr.split(sep or ".")
    obj = reduce(getattr, rattr[:-1], obj)
    delattr(obj, rattr[-1])
