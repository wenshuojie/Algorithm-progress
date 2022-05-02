# 889. 根据前序和后序遍历构造二叉树

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if not preorder:
            return

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        leftsize = postorder.index(preorder[1])+1
        root.left = self.constructFromPrePost(preorder[1:1+leftsize],postorder[:leftsize])
        root.right = self.constructFromPrePost(preorder[1+leftsize:],postorder[leftsize:len(postorder)-1])
        return root
