# 二叉树的中序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution:
    res = []
    def inorderTraversal(self , root: TreeNode) -> List[int]:
        sys.setrecursionlimit(1500)
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
        
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)