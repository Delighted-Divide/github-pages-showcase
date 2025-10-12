import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_positive_number():
    assert longest_positive_streak([1]) == 1

def test_single_non_positive_number():
    assert longest_positive_streak([-1]) == 0

def test_all_positive_numbers():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_streak_at_the_beginning():
    assert longest_positive_streak([5, 6, 7, 0, 4, -1, 2, 3]) == 3

def test_streak_at_the_end():
    assert longest_positive_streak([2, 3, -1, 5, 0, 4, 5, 6, 7]) == 4

def test_with_zeros():
    assert longest_positive_streak([1, 2, 0, 3, 4, 0, 5]) == 2
