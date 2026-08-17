"""
Utilities for checking whether two strings are anagrams.
"""

# Given two strings s and t, it returns true if t is an anagram of s, and false otherwise.


def is_anagram(s: str, t: str) -> bool:
    """
    Return True if t is an anagram of s, otherwise False.

    Two strings are anagrams when they contain the same characters
    with the same frequencies, but in a different order.

    Args:
        s: The original string to compare.
        t: The candidate anagram to check.

    Returns:
        True if t is an anagram of s, otherwise False.
    """

    # Write your code here

    # we check if both strings have the same length
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        count[char] = count.get(char, 0) - 1

    # this expression that loops in `count` checking, key by key, if the value of each key equals to zero.
    return all(value == 0 for value in count.values())


s = "anagram"

t = "nagaram"
