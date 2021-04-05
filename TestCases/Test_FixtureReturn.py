import pytest

@pytest.fixture()
def input():
        input=39
        return input

def test_div(input):
        assert input % 3  == 0
