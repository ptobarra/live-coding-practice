"""Linked list utilities for reversing a singly linked list.

This module defines a basic ListNode and a function that reverses
the order of nodes in a singly linked list in-place.
"""

# Given the head of a singly linked list, reverse the list and return the reversed list.


class ListNode:
    """Node for a singly linked list.

    Attributes:
        val: The value stored in the node.
        next: The next node in the linked list, or None if this is the tail.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    """
    Reverse a singly linked list and return the new head.

    This function iterates through the list, reassigning each node's `next`
    pointer to point to the previous node. The previous pointer tracks the
    reversed portion of the list, while the current pointer advances forward.

    Args:
        head: The head node of the linked list to reverse.

    Returns:
        The head of the reversed linked list.
    """
    # Write your code here
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# | Input | Output |
# | head = [1,2,3,4,5] | [5,4,3,2,1] |
# | head = [1,2] | [2,1] |
# | head = [] | [] |

# ---

# head = []

# | prev | current | next_node | current.next |
# | None | None | None | None |

# head = [1, 2]

# | prev | current | next_node | current.next |
# | None | 1 | - | 2 |
# | 1 | 2 | None | 1 |
# | 2 | None | - | - |
