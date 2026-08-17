"""Find all unique triplets in an integer list that sum to zero."""

# Given an array of integers nums, return all triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# For each fixed value, use a two-pointer search on the remaining sorted list
# to find pairs that complete a zero-sum triplet.


def three_sum(nums: list[int]) -> list[list[int]]:
    """Return all unique triplets whose values sum to zero.

    The input list is sorted in place, then a two-pointer search is used
    for each anchor value to find matching pairs efficiently.

    Args:
        nums: A list of integers.

    Returns:
        A list of unique triplets, where each triplet sums to zero.

    Notes:
        - Duplicate triplets are skipped.
        - The input list is modified because it is sorted in place.
    """
    # Write your code here
    nums.sort()
    result = []

    for i in range(len(nums)):
        # skip duplicate values of i
        # Skip duplicate anchors so each triplet is produced once.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:  # Stop condition
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # NOW skip duplicates at the new left/right positions
                # Skip repeated values after recording a valid triplet.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                # Increase the sum by moving the left pointer right.
                left += 1  # we increase the value of total
            else:
                # Decrease the sum by moving the right pointer left.
                right -= 1  # we decrease the value of total

    return result


# **Example 1:**

# * **Input:** `nums = [-1,0,1,2,-1,-4]`
# * **Output:** `[[-1,-1,2],[-1,0,1]]`
# * **Explanation:** Triplets that sum to zero: `[-1,-1,2]` and `[-1,0,1]`.

# **Example 2:**

# * **Input:** `nums = [0,1,1]`
# * **Output:** `[]`
# * **Explanation:** No valid triplets were found.

# **Example 3:**

# * **Input:** `nums = [0,0,0]`
# * **Output:** `[[0,0,0]]`
# * **Explanation:** The only valid triplet is `[0,0,0]`.
