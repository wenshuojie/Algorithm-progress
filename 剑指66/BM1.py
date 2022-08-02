# 反转链表

class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        pre = None
        curr = head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
        
        return pre

class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        # write code here
        if not head or not head.next:
            return head
        
        last = self.ReverseList(head.next)
        head.next.next = head
        head.next = None

        return last
