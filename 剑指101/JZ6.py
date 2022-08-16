# 从尾到头打印链表

class Solution:
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        node_list = []
        while listNode:
            node_list.append(listNode.val)
            listNode = listNode.next
            
        return node_list[::-1]