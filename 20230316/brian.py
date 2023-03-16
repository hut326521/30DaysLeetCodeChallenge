"""
Based on the characteristics of in- and pre-order traverse. We can have some
clues about our algorithm.
1. the last node in post-order is the root of the binary tree
2. when the root is found in post-order, we can spot it in in-order because
   all numbers are unique.
3. all numbers before the root in in-order belong to the left subtree;
   numbers after the root to the right subtree.
"""
from typing import List, Optional

from py_utils.tree import TreeNode


class Solution:
    def buildTree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        # edge cases
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        # root is the last number in postorder
        root = TreeNode(postorder[-1])
        # find the index of the root in inorder
        root_inorder_index = inorder.index(root.val)
        # nums before/after the root belong to the left/right subtree
        inorder_left_subtree = inorder[:root_inorder_index]
        inorder_right_subtree = inorder[root_inorder_index + 1:]
        # recursively build subtrees
        root.left = self.buildTree(
            inorder_left_subtree,
            postorder[:len(inorder_left_subtree)],
        )
        root.right = self.buildTree(
            inorder_right_subtree,
            postorder[len(inorder_left_subtree):-1],
        )
        return root
