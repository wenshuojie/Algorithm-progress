# 单链表的倒数第 k 个节点
# 只遍历一次

from tkinter.messagebox import NO


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def penultimatek(ListNode, k):
    p1, p2 = ListNode, ListNode
    for i in range(k):
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

print(penultimatek(p1,1).val)
    
