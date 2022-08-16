# 两个链表的第一个公共结点

class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        p1, p2 = pHead1, pHead2
        
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = pHead2
            if p2:
                p2 = p2.next
            else:
                p2 = pHead1
        
        return p1
