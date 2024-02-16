from calculator import add, sub

def test_addition():
    assert add(1, 2) == 3

def test_subtraction():
    assert sub(3, 3) == 6  # This test case will intentionally fail
