"""
Pytest suite for the longest_positive_streak function.
"""

import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test that a list with no positive numbers returns 0."""
    assert longest_positive_streak([-1, -5, 0, -10]) == 0

def test_all_positive_numbers():
    """Test a simple case with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_multiple_streaks_longest_in_middle():
    """Test that the longest of multiple streaks is correctly identified."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_longest_streak_at_beginning():
    """Test a case where the longest streak is at the start of the list."""
    assert longest_positive_streak([10, 20, 30, 40, -5, 1, 2]) == 4

def test_longest_streak_at_end():
    """Test a case where the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 0, 5, 8, 9, 12, 15]) == 5

def test_single_element_streaks():
    """Test with streaks of length 1."""
    assert longest_positive_streak([1, -1, 2, -2, 3, -3]) == 1

def test_list_with_only_zeros():
    """Test a list composed entirely of zeros."""
    assert longest_positive_streak([0, 0, 0, 0]) == 0
