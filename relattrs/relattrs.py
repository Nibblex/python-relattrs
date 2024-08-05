from functools import reduce
from typing import Any, Optional


def rgetattr(obj: object, rattr: str, sep: Optional[str] = None) -> Any:
    rattr = rattr.split(sep)
    return reduce(getattr, rattr, obj)


def rhasattr(obj: object, rattr: str, sep: Optional[str] = None) -> bool:
    rattr = rattr.split(sep)
    obj = reduce(getattr, rattr[:-1], obj)
    return hasattr(obj, rattr[-1])


def rsetattr(obj: object, rattr: str, val: Any, sep: Optional[str] = None) -> None:
    rattr = rattr.split(sep)
    obj = reduce(getattr, rattr[:-1], obj)
    setattr(obj, rattr[-1], val)


def rdelattr(obj: object, rattr: str, sep: Optional[str] = None) -> None:
    rattr = rattr.split(sep)
    obj = reduce(getattr, rattr[:-1], obj)
    delattr(obj, rattr[-1])
