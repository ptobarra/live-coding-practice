"""Solve the maximum subarray problem using Kadane's algorithm."""

# Given an array of integers nums, find the contiguous subarray that has the largest sum and return its sum.


def max_sub_array(nums: list[int]) -> int:
    """Return the largest sum of any contiguous subarray.

    This uses Kadane's algorithm in O(n) time and O(1) extra space.

    Args:
        nums: A non-empty list of integers.

    Returns:
        The maximum possible sum of a contiguous subarray.

    Raises:
        IndexError: If nums is empty.
    """
    # Write your code here
    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


# # Maximum Subarray Examples

# ## Example 1

# * **Input:** `nums = [-2,1,-3,4,-1,2,1,-5,4]`
# * **Output:** `6`
# * **Explanation:** The subarray `[4,-1,2,1]` has the largest sum of 6.

# ## Example 2

# * **Input:** `nums = [1]`
# * **Output:** `1`
# * **Explanation:** The subarray `[1]` has the largest sum of 1.

# ## Example 3

# * **Input:** `nums = [5,4,-1,7,8]`
# * **Output:** `23`
# * **Explanation:** The subarray `[5,4,-1,7,8]` has the largest sum of 23.

# # Considerations

# ## Starting fresh is better that extending when nums[i] > current_sum + nums[i]

#  ## Table

# | num | current_sum + num | current_sum | best_sum | choice | action |
# | --- | --- | --- | --- | --- | --- |
# | -2 | -- | -2 | -2 | current_sum + num | extend |
# | 1 | -1 | 1 | 1 | num | restart |
# | -3 | -2 | -2 | 1 | current_sum + num | extend |
# | 4 | 2 | 4 | 4 | num | restart |
# | -1 | 3 | 3 | 4 | current_sum + num | extend |
# | 2 | 5 | 5 | 5 | current_sum + num | extend |
# | 1 | 6 | 6 | 6 | current_sum + num | extend |
# | -5 | 1 | 1 | 6 | current_sum + num | extend |
# | 4 | 5 | 5 | 6 | current_sum + num | extend |

# best_num = max(num, current_sum + num)

# ## Initialization

# current_sum = nums[0]
# best_sum = current_sum
