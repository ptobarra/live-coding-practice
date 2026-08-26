# A robot on an m x n grid tries to reach the bottom right corner. Return the number of possible unique paths.


"""Compute the number of unique paths in an m x n grid.

A robot starts at the top-left corner and can move only right or down.
This file includes two dynamic programming solutions:

- `unique_paths_space_m_n`: uses a 2D grid and O(m * n) space.
- `unique_paths_time_m_n`: uses a 1D array and O(n) space.

Both solutions run in O(m * n) time.
"""


def unique_paths_space_m_n(m: int, n: int) -> int:
    """Return the number of unique paths in an m x n grid using O(m * n) space.

    The robot starts at the top-left corner and may move only right or down.
    This solution uses dynamic programming with a 2D grid where each cell stores
    the number of ways to reach that position from above or from the left.

    Time complexity: O(m * n)
    Space complexity: O(m * n)
    """
    # Write your code here
    paths = [[1] * n for _ in range(m)]

    for row in range(1, m):
        for col in range(1, n):
            paths[row][col] = paths[row - 1][col] + paths[row][col - 1]

    return paths[m - 1][n - 1]


def unique_paths_time_m_n(m: int, n: int) -> int:
    """Return the number of unique paths in an m x n grid using O(n) space.

    The robot starts at the top-left corner and may move only right or down.
    This solution uses dynamic programming with a 1D array that stores the
    number of ways to reach each column in the current row.

    Time complexity: O(m * n)
    Space complexity: O(n)
    """
    # Write your code here
    row_values = [1] * n  # row 0
    for row in range(1, m):
        for col in range(1, n):
            # your formula here
            row_values[col] = row_values[col] + row_values[col - 1]
    return row_values[n - 1]


# Unique Paths - Problem Details & Analogy

# | Section / Category | Detail |
# | :--- | :--- |
# | **Examples - Input** | `m = 3, n = 7` |
# | **Examples - Output** | `28` |
# | **Examples - Note** | There are 28 unique paths in a 3x7 grid. |
# | **Constraints** | `1 <= m, n <= 100` |
# | **Complexity** | • **Time:** `O(m * n)` • **Space:** `O(n)` |
# | **Analogy** | **Analogy: Robot in a warehouse** Robot must go from top-left corner to bottom-right corner moving only right/down. Paths to each position = ways to reach from top + ways from left. |
