# 重建二叉树

class Solution:
    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        if not pre:
            return
        
        root_val= pre[0]
        ind = vin.index(root_val)
        root = TreeNode(root_val)

        root.left = self.reConstructBinaryTree(pre[1:ind+1], vin[:ind])
        root.right = self.reConstructBinaryTree(pre[ind+1:], vin[ind+1:])
        return root
        