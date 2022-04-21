# 876. 链表的中间结点

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next: # 注意这里！！！判断fast.next的前提是fast不为空
            slow = slow.next
            fast = fast.next.next
        return slow