import pytest

from . import validate


def test_currency():
    assert validate.currency('bitcoin') is True
    with pytest.raises(ValueError):
        validate.currency('othercoin')
    with pytest.raises(ValueError):
        validate.currency('btc')
