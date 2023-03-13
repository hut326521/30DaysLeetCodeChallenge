"""
For this problem, it's straightforward that we can use recursion
to solve. We can compare the left and right nodes for their values first,
then compare two combinations.
1. left node's left versus right node's right
2. left node's right versus right node's left
"""
from typing import Optional

from py_utils.tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._compare_two_nodes(root.left, root.right)

    def _compare_two_nodes(
        self, left: Optional[TreeNode], right: Optional[TreeNode]
    ) -> bool:
        if left is None and right is None:
            return True
        left_value = left.val if left is not None else None
        right_value = right.val if right is not None else None
        if left_value != right_value:
            return False
        return (
            self._compare_two_nodes(left.left, right.right)
            and self._compare_two_nodes(left.right, right.left)
        )
