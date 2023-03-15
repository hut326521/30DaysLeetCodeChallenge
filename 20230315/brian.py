"""
We could use BFS to check the completeness layer by layer.
"""
from typing import Optional

from py_utils.tree import TreeNode


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        current_layer = [root]
        while current_layer:
            next_layer = []
            none_presented = False
            for node in current_layer:
                if node is None:
                    none_presented = True
                elif none_presented:
                    return False
                else:
                    next_layer.extend([node.left, node.right])
            if any(next_layer) and none_presented:
                return False
            current_layer = next_layer
        return True
