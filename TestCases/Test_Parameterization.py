import pytest

@pytest.mark.parametrize("num,out",[(1,11),(2,22),(3,35),(4,44)])
def test_mul(num,out):
    assert 11*num == out