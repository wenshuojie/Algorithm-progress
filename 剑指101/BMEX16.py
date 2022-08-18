# 二叉树的最近公共祖先

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p.val, q.val)

    def find(self, root, val1, val2): # p, q确保都在树中
        if not root:
            return
        
        if root.val == val1 or root.val == val2:
            return root
        
        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)
        if left and right:
            return root
        
        return left if left else right

class Solution:
    findo1, findo2 = False, False
    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        res = self.find(root, o1, o2)
        if not self.findo1 or not self.findo2:
            return
        return res
    
    def find(self, root, o1, o2): # p, q不确保都在树中
        # 所以不能遇到一个目标值就直接返回，而应该对二叉树进行完全搜索（后序位置）
        if not root:
            return

        left = self.lowestCommonAncestor(root.left, o1, o2)
        right = self.lowestCommonAncestor(root.right, o1, o2)
        if left and right:
            return root.val
        if root.val == o1 or root.val == o2:
            if root.val == o1:self.findo1 = True
            if root.val == o2:self.findo2 = True
            return root.val
        return left if left else right