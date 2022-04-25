# 反转链表前 N 个节点

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==1:
            return self.reverseN(head,n)
        head.next=self.reverseBetween(head.next,m-1,n-1)
        return head

    def reverseN(self,head,n):
        if n==1:
            self.successor=head.next
            return head
        last=self.reverseN(head.next,n-1)
        head.next.next=head
        head.next=self.successor
        return last
