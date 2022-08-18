class Solution:
    def isSymmetrical(self , pRoot: TreeNode) -> bool:
        return self.traverse(pRoot, pRoot)
    
    def traverse(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return self.traverse(root1.left, root2.right) and self.traverse(root1.right, root2.left)