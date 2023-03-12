from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def init_list(length: int, connection: Optional[int]) -> ListNode:
    head = last = ListNode(0)
    for i in range(1, length):
        new = ListNode(i)
        last.next = new
        last = new
    if connection is not None and connection >= 0:
        node = head
        for _ in range(connection):
            node = node.next
        last.next = node
    return head


def find_node_by_index(
    head: ListNode, index: Optional[int]
) -> Optional[ListNode]:
    if index is None:
        return None
    node = head
    for _ in range(index):
        node = node.next
    return node

def arr_to_linked_list(nums: List[int]) -> Optional[ListNode]:
    dummy = last = ListNode(-1)
    for num in nums:
        new = ListNode(num)
        last.next = new
        last = last.next
    return dummy.next
