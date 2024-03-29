class Solution:
    def mergeTrees(self , t1: TreeNode, t2: TreeNode) -> TreeNode:
        # write code here
        if not t1:
            return t2
        if not t2:
            return t1
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node