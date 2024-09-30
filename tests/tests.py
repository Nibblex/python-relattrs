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
    "attr_path, expected",
    [
        (["outer", "inner", "value"], 42),
        (["outer", "inner", "non_existent"], AttributeError),
        (["simple_value"], 10),
        (["non_existent"], AttributeError),
    ],
)
def test_rgetattr(container, sep, attr_path, expected):
    attr_path = sep.join(attr_path)
    if expected is AttributeError:
        # with default value
        assert rgetattr(container, attr_path, "default", sep=sep) == "default"

        # whitout default value
        with pytest.raises(AttributeError):
            rgetattr(container, attr_path, sep=sep)
    else:
        assert rgetattr(container, attr_path, sep=sep) == expected


@pytest.mark.parametrize("sep", separators)
@pytest.mark.parametrize(
    "attr_path, expected",
    [
        (["outer", "inner", "value"], True),
        (["outer", "inner", "non_existent"], False),
        (["simple_value"], True),
        (["non_existent"], False),
    ],
)
def test_rhasattr(container, sep, attr_path, expected):
    attr_path = sep.join(attr_path)
    assert rhasattr(container, attr_path, sep) == expected


@pytest.mark.parametrize("sep", separators)
@pytest.mark.parametrize(
    "attr_path, value",
    [
        (["outer", "inner", "value"], 100),
        (["outer", "inner", "new_attr"], "test"),
        (["simple_value"], 20),
        (["new_simple_attr"], "simple_test"),
    ],
)
def test_rsetattr(container, sep, attr_path, value):
    attr_path = sep.join(attr_path)
    rsetattr(container, attr_path, value, sep=sep)
    assert rgetattr(container, attr_path, sep=sep) == value


@pytest.mark.parametrize("sep", separators)
@pytest.mark.parametrize(
    "attr_path",
    [
        ["outer", "inner", "value"],
        ["outer", "inner", "non_existent"],
        ["simple_value"],
        ["non_existent"],
    ],
)
def test_rdelattr(container, sep, attr_path):
    attr_path = sep.join(attr_path)

    if "non_existent" in attr_path:
        with pytest.raises(AttributeError):
            rdelattr(container, attr_path, sep)
    else:
        rdelattr(container, attr_path, sep)
        assert not rhasattr(container, attr_path, sep)

    temp_attr = "outer.inner.temp" if sep == "." else "outer__inner__temp"
    rsetattr(container, temp_attr, "temporary", sep)
    assert rhasattr(container, temp_attr, sep)
    rdelattr(container, temp_attr, sep)
    assert not rhasattr(container, temp_attr, sep)


if __name__ == "__main__":
    pytest.main()
