# 判断一个链表是否为回文结构

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPail(self , head: ListNode) -> bool:
        if not head or not head.next:
            return head
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        head2 = self.reversed(slow)
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

    def reversed(self, head):
        pre, curr = None, head
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return curr
