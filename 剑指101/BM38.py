class Solution:
    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        if not root:
            return
        
        if root.val == o1 or root.val == o2:
            return root.val
        
        left = self.lowestCommonAncestor(root.left, o1, o2)
        right = self.lowestCommonAncestor(root.right, o1, o2)
        
        if left and right:
            return root.val
        return left if left else right
        