from typing import Optional

from py_utils.tree import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum_of_leaves(root, "")

    def sum_of_leaves(self, root: Optional[TreeNode], prefix: str) -> int:
        if root is None:
            return 0
        # the node is a leaf
        top_to_node = prefix + str(root.val)
        if root.left is None and root.right is None:
            return int(top_to_node)
        return self.sum_of_leaves(
            root.left, top_to_node
        ) + self.sum_of_leaves(
            root.right, top_to_node
        )
