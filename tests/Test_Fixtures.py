import pytest

@pytest.fixture()
def setup():
    print("Once before everymethod")
def testMethod1(setup):
    print("This is Test Method1")
def testMethod2():
    print("This is Test Method2")