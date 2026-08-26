"""House Robber II.

Given a list of house values arranged in a circle, return the maximum
amount that can be stolen without robbing two adjacent houses. Because the
first and last houses are neighbors, the circular case can be reduced to
two linear cases: rob houses from index 0 to n - 2, or from index 1 to n - 1.
The best result from those two scenarios is returned.
"""

# Houses in a circle: the first and last are adjacent. Return the maximum you can steal without alerting the police (not two adjacent houses).


def rob_linear(nums: list[int]) -> int:
    """Return the maximum amount that can be robbed from a linear street.

    This function solves the standard House Robber problem for a sequence
    where adjacent houses cannot both be robbed. It uses dynamic programming
    with rolling state variables to keep the time complexity at O(n) and the
    extra space at O(1).
    """
    prev = 0
    prev_prev = 0

    for i in range(len(nums)):
        current = max(prev, prev_prev + nums[i])
        prev_prev = prev
        prev = current
    return current


def rob(nums: list[int]) -> int:
    """Return the maximum amount that can be robbed from a circular street.

    If the list contains one house, that single house is the only valid option.
    Otherwise, the circular constraint means the first and last house cannot both
    be robbed, so we evaluate the two linear subproblems:
    - houses 0 through n - 2
    - houses 1 through n - 1

    The larger of the two results is returned.
    """
    if len(nums) == 1:
        return nums[0]
    else:
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# # House Robber II - Problem Details & Analogy

# | Section / Category | Detail |
# | :--- | :--- |
# | **Example 1 - Input** | `nums = [2,3,2]` |
# | **Example 1 - Output** | `3` |
# | **Example 1 - Note** | You cannot rob house 0 and house 2 at the same time. |
# | **Example 2 - Input** | `nums = [1,2,3,1]` |
# | **Example 2 - Output** | `4` |
# | **Example 3 - Input** | `nums = [1,2,3]` |
# | **Example 3 - Output** | `3` |
# | **Constraints** | • `1 <= nums.length <= 100` • `0 <= nums[i] <= 1000` |
# | **Complexity** | • **Time:** `O(n)` • **Space:** `O(1)` |
# | **Analogy** | **Analogy: Houses in a circle — you cannot rob neighbors** The houses form a ring: the first and last are neighbors. You solve two linear streets, ignoring one endpoint each time. |

# #### Step 2:

# As you cannot you house `0` and house `n -1` in a list of `n` houses; it is easier to solve the problem for 2 linear streets where the first and last houses can be robbed and choose the houses that yield the maximum amount out of the 2 streets.

# first street: from house `0` to house `n - 2`
# second street: from house `1` to house `n - 1`

# #### Step 3:

# - rob house `i`: `nums[i]`, but then house `i - 1` must have not been robbed.
# so my **total** is: `nums[i]] + (the best total achievable using only house up thorugh i - 2`

# - don't rob house `i`: **total** is unchanged from whatever the best was using houses up thorugh ` i - 1`. so i carry that number forward to the next index.

# therefore, the formula i should apply on each iterartion is:

# `best(i) = max(nums[i] + best(i - 2), best(i - 1))`

# #### Step 4:

# I want to track 2 variables:

# prev: best total using houses up through one house ago.

# prev_prev: best total using houses up through two houses ago.

# walking forweard, left to right, naturally gives me `prev_prev` and `prev` already computed by the time i need them.

# so the new formula for the new best is:

# `current = max(prev, prev_prev + nums[i]`

# so i either skip the house in position `i` (and carry forward `prev`), or i rob house `i` and add the result to whatever was best two houses back `prev_prev + nums[i]`

# then i would shift:
# ```python
# prev_prev = prev
# prev = current
# ```

# #### Step 6:

# if `nums=[5]`,  `nums[1:] = []` and `nums[:-1] = []`

# so at the beginning of my `rob` helper function i should check if i am handed an one lement list before calling `rob_linear`, and, in that case, return the only element in the original list.

# i will do no guardrails against houses with negative numbers.
