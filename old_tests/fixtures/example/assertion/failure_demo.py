import pytest
from pytest import raises


class TestRaises:
    def test(self):
        test_string = "This is a test string. Clearly not an integer."
        raises(TypeError, int, test_string)