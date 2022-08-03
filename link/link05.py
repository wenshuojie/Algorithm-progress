# 876. 链表的中间结点

from tkinter import N


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast.next and fast.next.next: # 注意这里！！！判断fast.next的前提是fast不为空
            slow = slow.next
            fast = fast.next.next
        return slow

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
# node3.next = node4

solution = Solution()
mid = solution.middleNode(node1)
print(mid.val)
