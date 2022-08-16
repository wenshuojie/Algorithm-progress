# 填充每个节点的下一个右侧节点指针

from typing import Optional
from queue import Queue

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution: # 层序
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        node_list = Queue()
        node_list.put(root)
        while not node_list.empty():
            row = []
            node_len = node_list.qsize()
            for _ in range(node_len):
                node = node_list.get()
                row.append(node)
                if node.left:
                    node_list.put(node.left)
                if node.right:
                    node_list.put(node.right)
            
            row_len = len(row)
            for i in range(row_len):
                if i == row_len-1:
                    row[i].next = None
                else:
                    row[i].next = row[i+1]
        
        return root

class Solution: # 三叉树遍历
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        self.traverse(root.left, root.right)
        return root
    
    def traverse(self, node1, node2):
        if not node1 or not node2:
            return
        node1.next = node2
        self.traverse(node1.left, node1.right)
        self.traverse(node1.right, node2.left)
        self.traverse(node2.left, node2.right)




