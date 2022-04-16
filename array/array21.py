# 83. 删除排序链表中的重复元素

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slow = head
        fast = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = fast
            fast = fast.next

        slow.next = None # 断开与后面重复元素的连接
        return head
            
