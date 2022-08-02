# 链表相加(二)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addInList(self , head1: ListNode, head2: ListNode) -> ListNode:
        