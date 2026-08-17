"""
Binary search implementation for finding a target value in a sorted list.
"""

# Given an array of integers nums that is sorted in ascending order, and a target integer, write a function to find the target in nums.


def search(nums: list[int], target: int) -> int:
    """
    Return the index of target in a sorted list of integers.

    Uses binary search to repeatedly narrow the search range by comparing
    the target with the middle element of the current range.

    Args:
        nums: A sorted list of integers.
        target: The integer value to find.

    Returns:
        The index of target if it exists in nums; otherwise -1.
    """
    # Write your code here

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((high - low) / 2) + low

        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1


# nums = [-1,0,3,5,9,12], target = 9 -> output == 4
# 9 exists in nums and its index is 4.
# | low | high | mid | nums[mid] | target | comparison | action |
# | 0 | 5 | 2 | 3 | 9 | False | 9 > 3 | low = 3 |
# | 3 | 5 | 4 | 9 | 9 | True | 9 == 9 | return 4 |

# nums = [-1,0,3,5,9,12], target = -1 -> output == -1
# 2 does not exist in nums so it returns '-1'.
# nums = [-1,0,3,5,9,12], target = 2
# | low | high | mid | nums[mid] | target | comparison | action |
# | 0 | 5 | 2 | 3 | 2 | 2 < 3 | high = 1 |
# | 0 | 1 | 0 | -1 | 2 | 2 > -1 | low = 1 |
# | 1 | 1 | 1 | 0 | 2 | 2 > 0 | low = 2 |
# | 2 | 1 | - | - | 2 | loop condition low <= high is false | exit loop, return -1 |

# nums = [5], target = 5 -> output == 0
# target found in index 0.
# | low | high | mid | nums[mid] | target | comparison | action |
# | 0 | 0 | 0 | 5 | 5 | 5 == 5 | return 0 |
