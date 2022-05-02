# 105. 从前序与中序遍历序列构造二叉树

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return

        root_val = preorder[0]
        rootind_of_inorder = inorder.index(root_val)
        # left_size = rootind_of_inorder

        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:1+rootind_of_inorder],inorder[:rootind_of_inorder])
        root.right = self.buildTree(preorder[1+rootind_of_inorder:],inorder[rootind_of_inorder+1:])

        return root