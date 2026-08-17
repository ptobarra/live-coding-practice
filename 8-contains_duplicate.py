"""Utilities for checking whether a list contains duplicate values."""

# Given an array of integers nums, it returns true if any value appears at least twice in the array, and returns false if all elements are distinct.


# def contains_duplicate(nums: list[int]) -> bool:
#     # Write your code here
#     pass


def contains_duplicate_look_if_in_set(nums: list[int]) -> bool:
    """
    Return True if any value appears more than once in nums.

    The function keeps a set of seen numbers and checks whether each new
    number has already been encountered.

    Args:
        nums: A list of integers.

    Returns:
        True if a duplicate is found; otherwise False.
    """
    # Write your code here
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_list_set_lenghts(nums: list[int]) -> bool:
    """
    Return True if the list contains duplicates.

    This approach compares the length of the original list with the length
    of a set built from its values. If the lengths differ, at least one
    duplicate value was removed when converting to a set.

    Args:
        nums: A list of integers.

    Returns:
        True if duplicates exist; otherwise False.
    """
    # Write your code here
    unique_nums = set(nums)
    return len(nums) != len(unique_nums)


# | input | output | comment |
# | nums = [1,2,3,1] | true | 1 repeats. |
# | nums = [1,2,3,4] | false | all distinct. |
# | nums = [1,1,1,3,3,4,3,2,4,2] | true | several values repeat. |
