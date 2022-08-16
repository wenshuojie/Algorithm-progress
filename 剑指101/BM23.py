# 二叉树的前序遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    res = []
    def preorderTraversal(self , root: TreeNode) -> List[int]:
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
        
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)