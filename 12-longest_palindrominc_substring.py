"""Find the longest palindromic substring using expand-around-center."""

# Given a string s, it returns the longest palindromic substring in s.


def expand_around_center(s: str, left: int, right: int) -> tuple[int, int]:
    """Expand outward from a center while the substring stays a palindrome.

    Args:
        s: The string to search within.
        left: Left index of the initial center (equal to `right` for an
            odd-length center, or `right - 1` for an even-length center).
        right: Right index of the initial center.

    Returns:
        A tuple `(start, end)` of inclusive indices bounding the longest
        palindrome found by expanding from this center.
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # loop just exited — at the moment any of the three conditions fail, the valid palindrome is `[left+1, right-1]`
    return (left + 1, right - 1)


def longest_palindrome(s: str) -> str:
    """Return the longest palindromic substring of s.

    This checks both odd-length and even-length centers for every index
    in O(n^2) time and O(1) extra space.

    Args:
        s: The string to search within.

    Returns:
        The longest contiguous palindromic substring of s. If several
        substrings share the maximum length, one of them is returned.
    """
    # Write your code here
    best_start, best_end = 0, 0  # or some other sensible starting boundaries

    for i in range(len(s)):
        # odd-length center at i
        left1, right1 = expand_around_center(s, i, i)
        # even-length center between i and i+1
        left2, right2 = expand_around_center(s, i, i + 1)

        # compare both results against the best found so far, update if longer

        if right1 - left1 > best_end - best_start:
            best_start = left1
            best_end = right1

        if right2 - left2 > best_end - best_start:
            best_start = left2
            best_end = right2

    return s[best_start : best_end + 1]


# **Examples**

# **Example 1:**

# * **Input:** `s = "babad"`
# * **Output:** `"bab"`
# * **Explanation:** Both 'bab' and 'aba' are valid answers.

# **Example 2:**

# * **Input:** `s = "cbbd"`
# * **Output:** `"bb"`
# * **Explanation:** The longest palindromic substring is 'bb'.

# **Example 3:**

# * **Input:** `s = "a"`
# * **Output:** `"a"`
# * **Explanation:** A single character is a palindrome.
