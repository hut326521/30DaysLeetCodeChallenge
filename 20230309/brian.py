"""
For this problem, it's classic and we can use Floyd algorithm to find the
intersection.
"""
from typing import Optional
from unittest import TestCase

from py_utils.linked_list import ListNode, init_list, find_node_by_index


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case: zero length list
        if head is None:
            return None

        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        # no cycle
        if fast.next is None or fast.next.next is None:
            return None
        # find the intersection
        tracer = head
        while tracer is not slow:
            tracer = tracer.next
            slow = slow.next
        return tracer


class TestSolution(TestCase):
    cases = {
        "example1": (4, 1),
        "example2": (2, 0),
        "example3": (1, None),
    }

    def test_detectCycle(self):
        for name, (length, connection) in self.cases.items():
            with self.subTest(msg=name):
                ll = init_list(length, connection)
                self.assertIs(
                    Solution().detectCycle(ll),
                    find_node_by_index(ll, connection),
                )
