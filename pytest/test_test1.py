import test1
import pytest


@pytest.mark.skip(reason="I dont want to run at the moment")
def test_calc_sum():
    result = test1.calc_sum(4, 5)
    assert result == 9


def test_calc_mul():
    result = test1.calc_mul(4, 5)
    assert result == 20
