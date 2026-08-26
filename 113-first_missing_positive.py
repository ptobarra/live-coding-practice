"""Find the smallest missing positive integer.

Given an unsorted array of integers, return the smallest positive integer
that is not present in the array. The solution runs in O(n) time and uses
O(1) extra space by placing each value into its "correct" index when possible.
"""

# Find the smallest missing positive integer in an unsorted array in O(n) time and O(1) space


# def first_missing_positive(nums):
#     # Write your code here
#     pass


def first_missing_positive(nums: list[int]) -> int:
    """Return the smallest missing positive integer in the array.

    The algorithm places each value x in its target slot at index x - 1,
    as long as x is between 1 and n. After the swaps, the first index where
    nums[i] != i + 1 reveals the answer. If all values 1..n are present,
    the answer is n + 1.
    """
    # Write your code here
    n = len(nums)

    for i in range(n):
        # the three conditions from your trace, combined
        while nums[i] != nums[nums[i] - 1] and nums[i] > 0 and nums[i] <= n:
            # perform the swap
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


# # Examples

# ### Example 1
# - **Input:** `nums = [1,2,0]`
# - **Output:** `3`
# - **Note:** 3 is missing

# ### Example 2
# - **Input:** `nums = [3,4,-1,1]`
# - **Output:** `2`
# - **Note:** 2 is missing

# ---

# # Constraints
# - `1 <= nums.length <= 10^5`
# - `-2^31 <= nums[i] <= 2^31 - 1`

# ---

# # Complexity
# - **Time:** $O(n)$
# - **Space:** $O(1)$

# ---

# # Analogy
# ### Analogy: Sorting tokens 1..n into their respective slots

# Each number goes to index `value - 1`; the first empty slot reveals the missing number.
