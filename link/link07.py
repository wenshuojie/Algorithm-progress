# 如果链表中含有环，如何计算这个环的起点

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head: ListNode):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None
    
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next
    
    return slow

p5 = ListNode(5)
p4 = ListNode(4,p5)
p3 = ListNode(3,p4)
p2 = ListNode(2,p3)
p1 = ListNode(1,p2)
p5.next = p2

print(detectCycle(p1).val)