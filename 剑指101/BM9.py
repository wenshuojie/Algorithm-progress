# 删除链表的倒数第n个节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self , head: ListNode, n: int) -> ListNode:
        p1, p2 = head, head

        vir = ListNode(-1)
        vir.next = head
        p3 = vir
        for _ in range(n):
            p1 = p1.next
        
        while p1:
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        
        temp = p2.next
        p3.next = temp

        return vir.next
