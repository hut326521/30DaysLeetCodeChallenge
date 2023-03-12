"""
Because the linked list is in ascending order, we know the best number for the
root of the height-balanced binary search tree is in the middle of the linked list.
Once we find the middle node, we can find its left child by applying the smae logic
to the first half of the list; right child to the second half.
"""
from math import ceil
from typing import Optional

from py_utils.linked_list import ListNode, arr_to_linked_list
from py_utils.tree import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = self._get_list_length(head)
        return self._sorted_list_to_bst_with_known_length(head, length)

    def _get_list_length(self, head: ListNode):
        count = 0
        node = head
        while node is not None:
            count += 1
            node = node.next
        return count

    def _sorted_list_to_bst_with_known_length(
        self, head: Optional[ListNode], length: int
    ):
        if not length:
            return None
        if length == 1:
            return TreeNode(head.val)
        center = ceil(length / 2)
        dummy_head = ListNode(0)
        dummy_head.next = head
        node = dummy_head
        for _ in range(center):
            node = node.next
        head_of_2nd_half = node.next
        left_node = self._sorted_list_to_bst_with_known_length(head, center - 1)
        right_node = self._sorted_list_to_bst_with_known_length(
            head_of_2nd_half, length - center
        )
        root = TreeNode(node.val, left_node, right_node)
        return root
