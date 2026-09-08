import pytest

from origins import origin, same_origin


@pytest.mark.parametrize(
    "other,expected",
    [
        ("https://lab.invalid/b?q=1#part", True),
        ("https://LAB.invalid:443/", True),
        ("http://lab.invalid/", False),
        ("https://lab.invalid:8443/", False),
        ("https://child.lab.invalid/", False),
    ],
)
def test_origin_boundary(other, expected):
    assert same_origin("https://lab.invalid/a", other) is expected


@pytest.mark.parametrize(
    "url",
    [
        "/relative",
        "file:///tmp/a",
        "https://a:b@lab.invalid/",
        "https://lab.invalid:99999/",
        "https://lab.invalid:/",
        "https://lab.invalid:0/",
        "https://[::1]/",
        "https://lab.invalid\\a",
        "https://lab.invalid/\n",
    ],
)
def test_reject_unsupported_syntax(url):
    with pytest.raises(ValueError):
        origin(url)
