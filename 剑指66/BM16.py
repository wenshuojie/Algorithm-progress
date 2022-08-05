# 删除有序链表中重复的元素-II

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        res = ListNode(-9999)
        res.next = head
        p = res

        while p.next and p.next.next:
            if p.next.val != p.next.next.val:
                p = p.next
            else:
                sim_val = p.next.val
                while p.next and p.next.val == sim_val:
                    p.next = p.next.next
        
        return res.next