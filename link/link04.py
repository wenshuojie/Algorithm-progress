# 19. 删除链表的倒数第 N 个结点

from dbm import dumb


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dumpy = ListNode(-1,head) # 虚拟节点技巧
        pre_del = self.penultimatek(dumpy, n+1)
        pre_del.next = pre_del.next.next
        return dumpy.next

    def penultimatek(self, head: ListNode, n: int):
        p1, p2 = head, head
        for _ in range(n):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2

p5 = ListNode(5,None)
p4 = ListNode(4,p5)
p3 = ListNode(3,p4)
p2 = ListNode(2,p3)
p1 = ListNode(1,p2)

solution = Solution()
solution.removeNthFromEnd(p1,3)




