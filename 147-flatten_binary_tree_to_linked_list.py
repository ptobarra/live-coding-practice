"""Flatten a binary tree into a linked list.

This module solves the "Flatten Binary Tree to Linked List" problem.
The tree is traversed in preorder, and each node is rewired so that:
- its left child is set to None
- its right child points to the next node in preorder order

The final structure is a right-skewed linked list that preserves the preorder
sequence of the original tree.
"""

# Given the root of a binary tree, flatten it into a linked list. The list uses the right nodes and follows preorder traversal (left always null).


class TreeNode:
    """Node in a binary tree."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode | None, values: list[TreeNode]) -> None:
    """Append each node in preorder order to the provided list.

    A node is visited before its left subtree and before its right subtree.
    If root is None, the branch is empty and the function stops.
    """
    # If root is None, that means there is no branch here.
    if root is None:
        return

    # Visit the current node first
    values.append(root)

    # Then walk the left subtree
    preorder_traversal(root.left, values)

    # Then walk the right subtree
    preorder_traversal(root.right, values)


def flatten(root: TreeNode) -> None:
    """Flatten a binary tree into a linked list using preorder traversal.

    The flattened list is built by collecting all nodes in preorder order,
    then re-linking each node's right pointer to the next node in that list.
    The left pointer of every node is cleared to satisfy the linked-list
    requirement.
    """
    # Write your code here
    if root is None:
        return

    nodes = []
    preorder_traversal(root, nodes)

    for i in range(len(nodes) - 1):
        nodes[i].left = None
        nodes[i].right = nodes[i + 1]

    nodes[-1].left = None
    nodes[-1].right = None


# # Examples

# ## Example 1
# - **Input:** `root = [1,2,5,3,4,null,6]`
# - **Output:** `[1,null,2,null,3,null,4,null,5,null,6]`
# - **Explanation:** Preorder 1-2-3-4-5-6 as a right-skewed linked list.

# ## Example 2
# - **Input:** `root = []`
# - **Output:** `[]`
# - **Explanation:** Empty tree.

# ---

# # Constraints

# - The number of nodes is in the range `[0, 2000]`.
# - `-100 <= Node.val <= 100`

# ---

# # Complexity

# - **Time Complexity:** O(n)
# - **Space Complexity:** O(1)


"""
This uses O(n) space for the traversal list — there's a known O(1) in-place technique using the Morris Traversal idea, which threads the right subtree's leftmost node back to the current node's right pointer as you go, avoiding the explicit list entirely, but it's considerably trickier to get right.
"""
