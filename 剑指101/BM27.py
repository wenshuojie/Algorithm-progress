# 按之字形顺序打印二叉树

from typing import List
from queue import Queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        if not pRoot:
            return []
        
        node_list = Queue()
        res = []
        layer = 1
        node_list.put(pRoot)

        while not node_list.empty():
            row = []
            q_size = node_list.qsize() # 最好是用一个变量存储当前的长度，因为有些语言len会动态变化
            for _ in range(q_size):
                node = node_list.get()
                if node.left:
                    node_list.put(node.left)
                if node.right:
                    node_list.put(node.right)
                row.append(node.val)
            if layer % 2 == 0:
                row = row[::-1]
            layer += 1
            res.append(row)
        
        return res

p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)

p1.left = p2
p1.right = p3
p3.left = p4
p3.right = p5

solution = Solution()
print(solution.Print(p1))