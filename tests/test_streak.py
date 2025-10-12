from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_and_negatives_break_streak():
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6]) == 2

def test_all_positive():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_no_positive():
    assert longest_positive_streak([-1, -2, 0, -3]) == 0
