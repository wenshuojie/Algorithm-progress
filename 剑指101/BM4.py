# 合并两个排序的链表

class Solution:
    def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        new_list = ListNode(-1)
        p1, p2, p3 = pHead1, pHead2, new_list
        
        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        
        if p1:
            p3.next = p1
        
        if p2:
            p3.next = p2
        
        return new_list.next