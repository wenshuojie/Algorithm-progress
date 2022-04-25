# 160. 相交链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        while pA != pB:
            if not pA:
                pA = headB
            else:
                pA = pA.next
            if not pB:
                pB = headA
            else:
                pB = pB.next

        return pA
