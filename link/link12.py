class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse(head): #后序遍历链表
    if not head:
        return
    traverse(head.next)
    print(head.val)

p5 = ListNode(5)
p4 = ListNode(4,p5)
p3 = ListNode(3,p4)
p2 = ListNode(2,p3)
p1 = ListNode(1,p2)

traverse(p1)
