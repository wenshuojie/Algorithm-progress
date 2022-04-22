# 判断链表是否包含环

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool : 
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

p5 = ListNode(5)
p4 = ListNode(4,p5)
p3 = ListNode(3,p4)
p2 = ListNode(2,p3)
p1 = ListNode(1,p2)
p5.next = None

print(hasCycle(p1))

