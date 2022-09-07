import pytest
import pandas as pd
from src.logic import roman_string_to_date_parser

def test_passes():
    assert True


def also_passes():
    VALUE = 1
    OTHER_VALUE = 1
    assert VALUE == OTHER_VALUE


def test_fails():
    assert False


def test_error():
    raise Exception('This is an error')


def test_catches_error():
    with pytest.raises(Exception):
        raise Exception('This is an error')


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


# I would often recommend starting with your tests before actually
# writing the code. This is called test driven development (TDD).
# This can save you a lot of time because of rapid testing of your
# implementation. It also helps you to think about the problem
# you are trying to solve and how you want to solve it. e.g: 
# Do we always expect the same delimiters?

# I created a test for the first number below, can you think of more 
# and build on it? hint: use the pytest.mark.parametrize decorator
def test_to_datetime():
    # Given / Arrange
    correct_date = pd.Timestamp(year=2012, month=1, day=1)
    # When / Act
    calculated_date = roman_string_to_date_parser('I.I.MMXII')
    # Then / Assert
    assert correct_date == calculated_date
