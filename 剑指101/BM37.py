#  二叉搜索树的最近公共祖先

class Solution:
    def lowestCommonAncestor(self , root: TreeNode, p: int, q: int) -> int:
        val1 = min(p, q)
        val2 = max(p, q)
        return self.traverse(root, val1, val2)

    def traverse(self, root, val1, val2):
        if not root:
            return
        
        if root.val < val1:
            return self.traverse(root.right, val1, val2)
        if root.val > val2:
            return self.traverse(root.left, val1, val2)
        return root.val

