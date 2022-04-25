# 206. 反转链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode: # 递归反转链表
        if not head or not head.next:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return last

    def reverseList_v2(self, head: ListNode) -> ListNode: # 迭代
        pre = None
        curr = head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        
        return pre