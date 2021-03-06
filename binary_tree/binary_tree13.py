# 652. 寻找重复的子树

from collections import defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        tree_num = defaultdict(int)
        res = []

        def traverse(root):
            nonlocal tree_num, res

            if not root:
                return "#"

            left = self.traverse(root.left)
            right = self.traverse(root.right)
            subtree = str(left)+','+str(right)+','+str(root.val)
            
            if tree_num[subtree] == 1:
                res.append(subtree)

            tree_num[subtree] += 1
            return subtree

        traverse(root)
        return res

    
