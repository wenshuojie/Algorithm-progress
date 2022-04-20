# 21. 合并两个有序链表
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        dumpy = ListNode() # 虚拟头节点
        p = dumpy

        while p1 and p2 :
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2

        return dumpy.next






