# 链表内指定区间反转

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        vir = ListNode(-1)
        vir.next = head

        pre, curr = vir, head
        for _ in range(m-1):
            curr = curr.next
            pre = pre.next
        node1 = pre
        node2 = curr

        if curr and pre:
            for _ in range(m, n+1):
                temp = curr.next
                curr.next = pre
                pre = curr
                curr = temp
            node1.next = pre
            node2.next = curr
        return vir.next