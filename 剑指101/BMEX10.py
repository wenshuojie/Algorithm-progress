# 寻找重复的子树

from collections import defaultdict
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    res = []
    memo = defaultdict(int)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # 1.要知道以自己为根的结构；2.要知道其它子树的结构
        self.travserse(root)
        return self.res

    def travserse(self, root):
        if not root:
            return '#'

        left = self.travserse(root.left)
        right = self.travserse(root.right)
        sub_tree = str(left) + ',' + str(right) + ',' + str(root.val)

        if self.memo[sub_tree] == 1:
            self.res.append(root)
        
        self.memo[sub_tree] += 1
        return sub_tree

node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(1)
node1.left = node2
node1.right = node3
solution = Solution()
print(solution.findDuplicateSubtrees(node1))
