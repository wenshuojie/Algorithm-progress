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

            left = traverse(root.left)
            right = traverse(root.right)
            subtree = str(left)+','+str(right)+','+str(root.val)
            
            if tree_num[subtree] == 1:
                res.append(root)

            tree_num[subtree] += 1
            return subtree

        traverse(root)
        return res

node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(1)
node1.left = node2
node1.right = node3
solution = Solution()
print(solution.findDuplicateSubtrees(node1))
