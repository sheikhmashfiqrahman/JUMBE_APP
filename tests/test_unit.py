import pytest
from app.services import jumble

# unit tests for the jumble function

def test_jumble_zero_shift():
    assert jumble("test 123!", 0) == "test 123"

def test_jumble_one_shift():
    assert jumble("test 123!", 1) == "uftu 123"

def test_jumble_large_shift():
    assert jumble("test 123!", 100) == "paop 123"

def test_jumble_full_cycle():
    assert jumble("test 123!", 26) == "test 123"

def test_jumble_preserve_digits_spaces():
    assert jumble("hello world 123!", 5) == "mjqqt btwqi 123"

def test_jumble_remove_special_characters():
    assert jumble("welcome!!!", 1) == "xfmdpnf"

def test_jumble_more():
    assert jumble("welcome", 1001) == "Shift error"



