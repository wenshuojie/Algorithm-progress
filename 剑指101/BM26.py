# 求二叉树的层序遍历

from typing import List
from queue import Queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        q = Queue()
        q.put(root)
        res = []

        while not q.empty():
            row = []
            q_size = q.qsize()
            for _ in range(q_size):
                node = q.get()
                row.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
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
print(solution.levelOrder(p1))