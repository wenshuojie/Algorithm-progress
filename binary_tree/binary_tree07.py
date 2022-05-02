# 654. 最大二叉树

from logging import root
from operator import index
from typing import List
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return

        root_val = max(nums)
        root_ind = nums.index(root_val)

        root = TreeNode(root_val)
        root.left = self.constructMaximumBinaryTree(nums[:root_ind])
        root.right = self.constructMaximumBinaryTree(nums[root_ind+1:])

        return root


