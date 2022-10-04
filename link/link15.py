class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(n):
    head = ListNode()
    curptr = head

    for i in range(1, n):
        curptr.next = ListNode(i)
        curptr = curptr.next
    
    return head

def printList(head):
    if not head:
        print([])

    res = []
    while head:
        res.append(head.val)
        head = head.next
    
    print(res)
    # return res

def reverseListByTraverse(head): # （遍历）反转链表
    if not head:
        return head

    pre, cur = None, head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

def reverseListByRecursion(head): # （递归）反转链表
    if not head or not head.next:
        return head
    new_head = reverseListByRecursion(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverseListNByTraverse(head, n): # （遍历）反转链表前N个元素
    if not head:
        return head
    
    pre, cur = None, head
    for _ in range(n):
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    head.next = next
    return pre

def reverseListNByRecursion(head, n): # （递归）反转链表前N个元素
    if n == 1:
        temp = head.next
        return head, temp
    
    new_head, temp = reverseListNByRecursion(head.next, n-1)
    head.next.next = head
    head.next = temp

    return new_head, temp

# temp = None
def reverseListNByRecursion(head, n): # （递归）反转链表前N个元素
    global temp
    if n == 1:
        temp = head.next
        return head
    
    new_head = reverseListNByRecursion(head.next, n-1)
    head.next.next = head
    head.next = temp

    return new_head

def reverseBetweenByTraverse(head, m, n): # （遍历）反转链表部分元素
    if not head or n < m:
        return
    
    ptr1, ptr2 = head, None
    for _ in range(m-2):
        ptr1 = ptr1.next
    ptr2 = ptr1.next
    
    pre, cur = ptr1, ptr2
    for _ in range(m, n+1):
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    
    ptr1.next = pre
    ptr2.next = cur

    return head

def reverseBetweenByRecursion(head, m, n): # （递归）反转链表部分元素
    if m == 1:
        return reverseListNByRecursion(head, n)[0]
    
    head.next = reverseBetweenByRecursion(head.next, m-1, n-1)
    return head

def reverseab(a, b): # 反转[a,b)之间的元素，反转后a不指向b
    pre, cur, next = None, a, None
    while cur != b:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

def reverseListByGrop(head, k):
    if not head:
        return head
    
    a, b = head, head
    for _ in range(k):
        b = b.next
        if not b:
            return head
    
    new_head = reverseab(a, b)
    a.next = reverseListByGrop(b, k)
    return new_head



if __name__ == "__main__":
    head = createList(8)
    printList(head)

    # new_head = reverseListNByTraverse(head, 3)
    # printList(new_head)

    # new_head = reverseBetweenByRecursion(head, 3, 5)
    # printList(head)

    new_head = reverseListByGrop(head, 3)
    printList(new_head)
