# 合并k个已排序的链表

from queue import PriorityQueue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 难点在于，如何快速得到 k 个节点中的最小节点，接到结果链表上 => 最小堆
class Solution:
    def mergeKLists(self , lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        vir = ListNode(-1)
        p = vir
        ass_pq = PriorityQueue() # 辅助优先级队列（最小堆）
        
        for i in range(len(lists)):
            if lists[i]:
                ass_pq.put((lists[i].val, i))
#                 lists[i] = lists[i].next
        
        while not ass_pq.empty():
            val, idx = ass_pq.get()
            p.next = lists[idx]
            p = p.next
            
            if lists[idx].next:
                lists[idx] = lists[idx].next
                ass_pq.put((lists[idx].val, idx))
                
        return vir.next

        