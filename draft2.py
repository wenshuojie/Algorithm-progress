from turtle import right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self , pRoot: TreeNode) -> bool:
        if not pRoot:
            return
        
        left = self.serialize(pRoot.left)
        right = self.serialize(pRoot.right)
        if left == right[::-1]:
            return True
        else:
            return False
        
    def serialize(self, node, res=[]):
        if not node:
            return
        
        self.serialize(node.left)
        res.append(node.val)
        self.serialize(node.right)
        return res