class Solution:
    def IsBalanced_Solution(self , pRoot: TreeNode) -> bool:
        if not pRoot:
            return True
        
        left = self.depth(pRoot.left)
        right = self.depth(pRoot.right)
        if abs(left - right) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and \
                self.IsBalanced_Solution(pRoot.right)

    def depth(self, root): # 计算一个节点的深度
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return left + 1 if left > right else right + 1