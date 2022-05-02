# 106. 从中序与后序遍历序列构造二叉树

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return

        root_val = postorder[-1]
        rootindex_of_inorder = inorder.index(root_val)

        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:rootindex_of_inorder],postorder[:rootindex_of_inorder])
        root.right = self.buildTree(inorder[rootindex_of_inorder+1:],postorder[rootindex_of_inorder:len(postorder)-1])

        return root