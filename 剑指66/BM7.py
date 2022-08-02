# 链表中环的入口结点

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast, slow = pHead, pHead
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        if not fast or not fast.next:
            return None
        
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return fast