"""Solve the climbing stairs problem using bottom-up dynamic programming."""

# You are climbing a staircase. It takes n steps to reach the top. Each time you can climb 1 or 2 steps. In how many different ways can you climb to the top?


def climb_stairs(n: int) -> int:
    """Return the number of distinct ways to climb to step n.

    At each step you may climb 1 or 2 steps at a time, so ways(n) follows
    the Fibonacci recurrence ways(n) = ways(n - 1) + ways(n - 2). This
    computes it iteratively in O(n) time and O(1) extra space.

    Args:
        n: The total number of steps in the staircase (n >= 0).

    Returns:
        The number of distinct ways to reach step n.
    """
    # Write your code here
    if n <= 1:
        return 1

    prev_prev = 1  # ways(0)
    prev = 1  # ways(1)

    for step in range(2, n + 1):
        # ways(n) = ways(n - 2) + ways (n -1)
        current = prev_prev + prev  # your formula here

        # now shift prev_prev and prev forward for the next iteration
        prev_prev = prev  # ways(n - 2) = ways(n - 1)
        prev = current  # ways(n - 1) = ways(n)

    return current


# | n | ways(n-2) | ways(n-1) | ways(n) |
# | --- | --- | --- | --- |
# | 0 | -- | -- | 1 |
# | 1 | -- | 1 | 1 |
# | 2 | 1 | 1 | 2 |
# | 3 | 1 | 2 | 3 |
# | 4 | 2 | 3 | 5 |
# | 5 | 3 | 5 | 8 |

# **Examples**

# **Example 1:**

# * **Input:** `n = 2`
# * **Output:** `2`
# * **Explanation:** Two ways: 1 step + 1 step, or 2 steps.

# **Example 2:**

# * **Input:** `n = 3`
# * **Output:** `3`
# * **Explanation:** Three ways: 1+1+1, 1+2, or 2+1.

# **Example 3:**

# * **Input:** `n = 4`
# * **Output:** `5`
# * **Explanation:** Five ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2.
