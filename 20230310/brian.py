"""
The most straightforward method to randomly pick one node from
a linked list is to store its length, then pick one index within
[0, length) interval.
Optimized solution is to use so-called Algorithm R. But I couldn't
prove that the distribution is randomized. (shrug)
"""
from random import randrange
from typing import Optional

from py_utils.linked_list import ListNode

class Solution:
    head: Optional[ListNode] = None
    length: int = 0

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self._count_length()

    def _count_length(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        self.length = count

    def getRandom(self) -> int:
        index = randrange(0, self.length)
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val
