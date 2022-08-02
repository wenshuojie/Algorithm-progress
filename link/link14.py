# 86. 分隔链表

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        more = ListNode()
        less = ListNode()
        p_less = less
        p_more = more

        p = head
        while p is not None:
            if p.val < x:
                p_less.next = p
                p_less = p_less.next
                p = p.next
                p_less.next = None
            else:
                p_more.next = p
                p_more = p_more.next
                p = p.next
                p_more.next = None
        p_less.next = more.next
        return less.next


        