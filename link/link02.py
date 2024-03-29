# 23. 合并K个升序链表
from typing import Optional, List
from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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