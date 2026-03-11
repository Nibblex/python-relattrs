import pytest

from relattrs import rdelattr, rgetattr, rhasattr, rsetattr


class Inner:
    def __init__(self):
        self.value = 42


class Outer:
    def __init__(self):
        self.inner = Inner()


class Container:
    def __init__(self):
        self.outer = Outer()
        self.simple_value = 10


@pytest.fixture
def container():
    return Container()


separators = [".", "__", "|", " "]


@pytest.mark.parametrize("sep", separators)
@pytest.mark.parametrize(
    ("attr_path", "expected"),
    [
        (["outer", "inner", "value"], 42),
        (["outer", "inner", "non_existent"], AttributeError),
        (["outer", "non_existent", "value"], AttributeError),
        (["simple_value"], 10),
        (["non_existent"], AttributeError),
        ([""], AttributeError),
    ],
)
def test_rgetattr(container, sep, attr_path, expected):
    attr_path = sep.join(attr_path)
    if expected is AttributeError:
        # whitout default value
        with pytest.raises(AttributeError):
            rgetattr(container, attr_path, sep=sep)

        # with default value
        assert rgetattr(container, attr_path, "default", sep=sep) == "default"

    else:
        assert rgetattr(container, attr_path, sep=sep) == expected


@pytest.mark.parametrize("sep", separators)
@pytest.mark.parametrize(
    ("attr_path", "expected"),
    [
        (["outer", "inner", "value"], True),
        (["outer", "inner", "non_existent"], False),
        (["outer", "non_existent", "value"], False),
        (["simple_value"], True),
        (["non_existent"], False),
        ([""], False),
    ],
)
def test_rhasattr(container, sep, attr_path, expected):
    attr_path = sep.join(attr_path)
    assert rhasattr(container, attr_path, sep=sep) == expected


@pytest.mark.parametrize("sep", separators)
@pytest.mark.parametrize(
    ("attr_path", "value", "raises"),
    [
        (["outer", "inner", "value"], 100, False),
        (["outer", "inner", "new_attr"], "test", False),
        (["outer", "non_existent", "value"], 200, True),
        (["simple_value"], 20, False),
        (["new_simple_attr"], "simple_test", False),
        ([""], "test", False),
    ],
)
def test_rsetattr(container, sep, attr_path, value, raises):
    attr_path = sep.join(attr_path)
    if raises:
        with pytest.raises(AttributeError):
            rsetattr(container, attr_path, value, sep=sep)

    else:
        rsetattr(container, attr_path, value, sep=sep)
        assert rgetattr(container, attr_path, sep=sep) == value


@pytest.mark.parametrize("sep", separators)
@pytest.mark.parametrize(
    ("attr_path", "raises"),
    [
        (["outer", "inner", "value"], False),
        (["outer", "inner", "non_existent"], True),
        (["outer", "non_existent", "value"], True),
        (["simple_value"], False),
        (["non_existent"], True),
        ([""], True),
    ],
)
def test_rdelattr(container, sep, attr_path, raises):
    attr_path = sep.join(attr_path)

    if raises:
        with pytest.raises(AttributeError):
            rdelattr(container, attr_path, sep=sep)

    else:
        rdelattr(container, attr_path, sep=sep)
        assert not rhasattr(container, attr_path, sep=sep)

    temp_attr = sep.join(["outer", "inner", "temp_attr"])
    rsetattr(container, temp_attr, "temporary", sep=sep)
    assert rhasattr(container, temp_attr, sep=sep)
    rdelattr(container, temp_attr, sep=sep)
    assert not rhasattr(container, temp_attr, sep=sep)
