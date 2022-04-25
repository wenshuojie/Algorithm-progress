# 234. 回文链表
from audioop import reverse


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        return self.traverse(head)

    def traverse(self, right):
        if not right:
            return True # 只有一个节点
        
        res = self.traverse(right.next)
        res = res and (self.left.val == right.val)
        self.left = self.left.next
        return res

# 优化空间复杂度，通过迭代的方式判断
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # step1: 先找中间节点
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast: # 奇数情况，回文从中间节点的下一个节点开始
            slow = slow.next

        # step2: 反转以中间节点为首的链表
        left = head
        right = self.reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True

    def traverse(self, right):
        if not right:
            return True # 只有一个节点
        
        res = self.traverse(right.next)
        res = res and (self.left.val == right.val)
        self.left = self.left.next
        return res

    def reverse(self, head):
        pre, cur, next = None, head, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre

