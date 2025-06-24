import pytest

@pytest.fixture()
def input_func():
        input=39
        return input

def test_div(input_elem):
        assert input_elem % 3  == 0
