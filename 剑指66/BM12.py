# 单链表的排序

from typing import List

from torch import le


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# PriorityQueue
class Solution:
    def sortInList(self , head: ListNode) -> ListNode:
        from queue import PriorityQueue
        pq = PriorityQueue()
        
        while head:
            pq.put(head.val)
            head = head.next
        
        vir = ListNode(-1)
        p = vir
        while not pq.empty():
            p.next = ListNode(pq.get())
            p = p.next
        
        return vir.next

# sort
class Solution:
    def sortInList(self , head):
        temp = []
        p = head
        while p:
            temp.append(p.val)
            p = p.next
        
        temp.sort()
        p = head
        for i in range(len(temp)):
            p.val = temp[i]
            p = p.next
        
        return head

# 归并
class Solution:
    def sortInList(self , head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None # 断开

        left = self.sortInList(head)
        right = self.sortInList(mid)

        # 后序位置：归并
        res = ListNode(-1)
        p = res
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        if left:
            p.next = left
        if right:
            p.next = right
        return res.next



