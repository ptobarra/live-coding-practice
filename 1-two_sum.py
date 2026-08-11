# Given an array of integers nums and a target integer, return the indices of the two numbers that add up to the target.


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Return the indices of two numbers in nums that add up to target.

    Args:
        nums: A list of integers to search.
        target: The target sum to find.

    Returns:
        A list containing the indices of the two matching numbers,
        or an empty list if no such pair exists.
    """

    # Create an empty dict called something like seen — it will map value → index.
    seen = {}

    # Loop through nums with both index and value (enumerate).
    for i, num in enumerate(nums):
        # For each value, compute complement = target - value.
        complement = target - num

        # Check: is complement already a key in seen?
        # If yes → you found your pair. Return [seen[complement], current_index].
        if complement in seen:
            return [seen[complement], i]  # seen[complement] is an index, i is an index
        # If no → store the current value and index in seen, and keep going.
        seen[num] = i  # store: this value → this index

    return []  # or raise ValueError("No two sum solution found")
