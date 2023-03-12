"""
Because the given sets of linked list are all sorted ascending, we can focus on
the first nodes of each linked list to compare values. However, comparing the
first nodes from each list is time-consuming (O(n) where n is the number of
sets of linked list). Furthermore, we only care about the smallest one. This
hints us about the usage of "heap".
"""
import heapq
from typing import Optional, List, Tuple

from py_utils.linked_list import ListNode


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        # initialize the heap
        # the data structure in the heap is
        # (node_value, index_in_lists)
        # noted that `node_value` is only for sorting purpose.
        # first set of data in heap would be the first items of each l-list
        heap: List[Tuple[int, int]] = [
            (node.val, index)
            for index, node in enumerate(lists)
            if node is not None
        ]
        heapq.heapify(heap)
        # initialize a dummy head for the end result
        dummy_head = last_node = ListNode(0)
        # loop until nothing in the heap
        while heap:
            # Find the node with the minimum value from the heap
            _, candidate_index = heapq.heappop(heap)
            candidate = lists[candidate_index]
            if candidate.next is not None:
                lists[candidate_index] = candidate.next
                heapq.heappush(heap, (candidate.next.val, candidate_index))
            last_node.next = candidate
            last_node = last_node.next
            last_node.next = None

        return dummy_head.next
