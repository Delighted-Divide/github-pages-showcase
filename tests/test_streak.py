from streak import longest_positive_streak

def test_empty():
    assert longest_positive_streak([]) == 0

def test_all_positive_single_streak():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks_longest_wins():
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, 6, -1]) == 4

def test_zeros_and_negatives_break():
    assert longest_positive_streak([0, -1, 1, 2, 0, 3]) == 2
