# 链表中倒数最后k个结点

class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        # write code here
        p1, p2 = pHead, pHead
        count = 0
        for _ in range(k):
            if p1:
                p1 = p1.next
                count += 1

        if not p1 and count < k: # p1为空时，有两种情况：（1）非法情况count < k；（2）合法情况count >= k
            return None

        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2