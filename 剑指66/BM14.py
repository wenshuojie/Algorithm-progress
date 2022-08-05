#  链表的奇偶重排

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self , head: ListNode) -> ListNode:
        even = ListNode(0)
        odd = ListNode(1)
        p_even = even
        p_odd = odd
        count = 1

        while head:
            if count % 2 == 0:
                p_even.next = head
                p_even = p_even.next
            else:
                p_odd.next = head
                p_odd = p_odd.next
            head = head.next
            count += 1

        p_even.next = None
        p_odd.next = even.next
        return odd.next

# 双指针
class Solution:
    def oddEvenList(self , head: ListNode) -> ListNode:
        if not head:
            return head
        
        odd, even = head, head.next
        evenhead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        
        return head
        
        
