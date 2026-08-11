# You are given the headers of two ordered linked lists, list1 and list2. Merge the two lists into a single ordered list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Recursive solution: O(n+m)-space version
def merge_two_lists_recursive(
    list1: ListNode | None, list2: ListNode | None
) -> ListNode | None:
    """
    Merge two sorted linked lists into one sorted linked list.

    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.
    """
    # Write your code here
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1

    list2.next = merge_two_lists_recursive(list2.next, list1)
    return list2


# Iterative solution: O(1)-space version
def merge_two_lists(list1, list2):
    """
    Merge two sorted linked lists into a single sorted linked list using
    constant extra space.

    Args:
        list1: The head of the first sorted linked list.
        list2: The head of the second sorted linked list.

    Returns:
        The head of the merged sorted linked list.
    """
    dummy = ListNode()
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # one of the two lists still has leftover nodes — attach the rest, in one shot
    tail.next = list1 if list1 is not None else list2

    return dummy.next
