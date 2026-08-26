"""Find the majority element in an array.

The majority element is the value that appears more than n / 2 times.
This implementation uses the Boyer-Moore voting algorithm to achieve
O(n) time and O(1) space.

The problem guarantees that a majority element always exists.
"""

# Given an array of n elements, find the most frequent element (the one that appears more than n/2 times). You can assume it always exists. Do this in O(n) time and O(1) space.


def majority_element(nums: list[int]) -> int | None:
    """Return the majority element in nums.

    Uses the Boyer-Moore voting algorithm to find the element that appears
    more than n/2 times.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    # Write your code here
    candidate: int | None = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# # Majority Element - Problem Details

# | Section / Category | Detail |
# | :--- | :--- |
# | **Example 1 - Input** | `nums = [3,2,3]` |
# | **Example 1 - Output** | `3` |
# | **Example 1 - Note** | 3 appears 2 times out of 3 (> n/2). |
# | **Example 2 - Input** | `nums = [2,2,1,1,1,2,2]` |
# | **Example 2 - Output** | `2` |
# | **Example 2 - Note** | 2 appears 4 times out of 7 (> n/2). |
# | **Constraints** | • `n == nums.length • `1 <= n <= 5 * 10^4` • `-10^9 <= nums[i] <= 10^9` • A majority element always exists |
# | **Complexity** | • **Time:** `O(n)` • **Space:** `O(1)` |
