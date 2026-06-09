from functools import reduce
from typing import Any, Optional

__all__ = ["rgetattr", "rhasattr", "rsetattr", "rdelattr"]


def rgetattr(obj: object, rattr: str, /, *default, sep: Optional[str] = None) -> Any:
    """
    Recursively gets an attribute from an object using a dotted string path.

    Args:
        obj: The object from which to retrieve the attribute.
        rattr: The dotted string representation of the attribute to retrieve.
        default: The default value to return if the attribute does not exist.
        sep: The separator used to split the string representation. Defaults to '.'.

    Returns:
        Any: The value of the attribute.

    Raises:
        AttributeError: If the attribute does not exist and no default is provided.
        TypeError: If more than one default value is provided.

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

    if len(default) > 1:
        raise TypeError(
            f"rgetattr expected at most 1 default value, got {len(default)}"
        )

    parts = rattr.split(sep or ".")
    if default:
        try:
            return reduce(getattr, parts, obj)
        except AttributeError:
            return default[0]

    return reduce(getattr, parts, obj)


def rhasattr(obj: object, rattr: str, /, *, sep: Optional[str] = None) -> bool:
    """
    Recursively checks if an object has an attribute using a dotted string path.

    Args:
        obj: The object to check.
        rattr: The dotted string representation of the attribute to check.
        sep: The separator used to split the string representation. Defaults to '.'.

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

    parts = rattr.split(sep or ".")
    try:
        obj = reduce(getattr, parts[:-1], obj)
        return hasattr(obj, parts[-1])
    except AttributeError:
        return False


def rsetattr(
    obj: object, rattr: str, val: Any, /, *, sep: Optional[str] = None
) -> None:
    """
    Recursively sets an attribute on an object based on a dotted string representation.

    Args:
        obj: The object on which to set the attribute.
        rattr: The dotted string representation of the attribute to set.
        val: The value to set.
        sep: The separator used to split the string representation. Defaults to '.'.

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

    parts = rattr.split(sep or ".")
    obj = reduce(getattr, parts[:-1], obj)
    setattr(obj, parts[-1], val)


def rdelattr(obj: object, rattr: str, /, *, sep: Optional[str] = None) -> None:
    """
    Recursively deletes an attribute from an object using a dotted string path.

    Args:
        obj: The object from which to delete the attribute.
        rattr: The dotted string representation of the attribute to delete.
        sep: The separator used to split the string representation. Defaults to '.'.

    Example:
        >>> from relattrs import rdelattr, rhasattr
        >>> class A:
        ...     class B:
        ...         class C:
        ...             value = 1
        >>> obj = A()
        >>> rdelattr(obj, "B.C.value")
        >>> rhasattr(obj, "B.C.value")
        False
    """

    parts = rattr.split(sep or ".")
    obj = reduce(getattr, parts[:-1], obj)
    delattr(obj, parts[-1])
