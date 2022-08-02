# 链表相加(二)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addInList(self , head1: ListNode, head2: ListNode) -> ListNode:
        last1 = self.reversed(head1)
        last2 = self.reversed(head2)

        res_link = ListNode(-1)
        res = res_link

        mark = 0 # 只要用了mark就要立马归0
        while last1 and last2:
            val = last1.val + last2.val + mark
            if val >= 10:
                mark = 1
            else:
                mark = 0
            res.next = ListNode(val%10)
            res = res.next
            last1 = last1.next
            last2 = last2.next
        
        while last1:
            val = last1.val + mark
            mark = 0
            res.next = ListNode(val%10)
            res = res.next
            if val >= 10 and last1.next:
                mark = 1
            elif val >= 10 and not last1.next:
                res.next = ListNode(1)
                res = res.next
            last1 = last1.next
        
        while last2:
            val = last2.val + mark
            mark = 0
            res.next = ListNode(val%10)
            res = res.next
            if val >= 10 and last2.next:
                mark = 1
            elif val >= 10 and not last2.next:
                res.next = ListNode(1)
                res = res.next
            last2 = last2.next

        return self.reversed(res_link.next)

    def reversed(self, head):
        pre, curr = None, head
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

node1 = ListNode(0)
node2 = ListNode(6)
node3 = ListNode(3)


node2.next = node3

solution = Solution()
solution.addInList(node1, node2)

{9,6,5,7,0,1,0,5,6,6,0,1,3,7,5,2,3,9,4,6,8,6,7,5,1,3,1,9,4,6,6,7,1,2,0,7,7,2,5,8,1,1}
{9,6,5,7,0,1,0,5,6,6,0,1,3,7,5,2,3,9,4,6,8,6,7,5,1,3,1,9,4,6,7,7,1,2,0,7,7,2,5,8,1,1}