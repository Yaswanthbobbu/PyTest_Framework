import pytest

@pytest.mark.skip
def test_first():
    print("This is skipped")

@pytest.mark.xfail
def test_second():
    num = 100
    assert num > 20
@pytest.mark.xfail
def test_third():
    assert True