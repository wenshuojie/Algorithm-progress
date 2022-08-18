class Solution:
    def isValidBST(self , root: TreeNode) -> bool:
        # write code here
        return self.traverse(root, None, None)
    
    def traverse(self, root, min, max):
        if not root:
            return True
        
        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        return self.traverse(root.left, min, root) and \
                self.traverse(root.right, root, max)