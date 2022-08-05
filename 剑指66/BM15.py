#  删除有序链表中重复的元素-I

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        if not head:
            return head
        
        res, p = head, head
        
        while p:
            if res.val == p.val:
                p = p.next
            else:
                res.next = p
                res = res.next
                p = p.next
        res.next = None
        return head