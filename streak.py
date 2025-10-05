"""
This module provides a function to find the longest streak of positive numbers.
"""

def longest_positive_streak(nums: list[int]) -> int:
    """
    Calculates the length of the longest run of consecutive values
    strictly greater than 0.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest positive streak. Returns 0 for an empty list.
    """
    max_streak = 0
    current_streak = 0

    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            # When a non-positive number is found, the streak is broken.
            # Update the max_streak with the length of the streak that just ended.
            max_streak = max(max_streak, current_streak)
            # Reset the current streak counter.
            current_streak = 0

    # Final check to account for a streak that continues to the end of the list.
    return max(max_streak, current_streak)
