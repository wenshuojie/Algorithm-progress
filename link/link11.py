# 25. K 个一组翻转链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 反转链表
    def reverse(self,head):
        pre, cur, next = None, head, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    # 反转[head,b)之间的元素，反转后head不指向b
    def reverseab(self, head, b):
        pre, cur, next = None, head, None
        while cur != b:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverseKGroup(self, head, k):
        if not head:
            return head
        a, b = head, head
        for i in range(k):
            if not b:
                return head
            b = b.next

        newHead = self.reverseab(a, b)
        a.next = self.reverseKGroup(b,k)
        return newHead

