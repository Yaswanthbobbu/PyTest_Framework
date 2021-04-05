import pytest
import math

@pytest.mark.great
def test_first():
    num = 100
    assert num > 230

@pytest.mark.great
def test_second():
    num = 100
    assert num > 200
@pytest.mark.great
def test_third():
    assert False