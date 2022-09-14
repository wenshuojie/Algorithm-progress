class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self , pRoot: TreeNode) -> bool:
        if not pRoot:
            return True

        if self.traverse1(root) == self.traverse2(root):
            return True
        else:
            return False

    def traverse1(self, root, res=[]):
        if not root:
            return
        res.append(root.val)
        self.traverse1(root.left)
        self.traverse1(root.right)
        return res

    def traverse2(self, root, res=[]):
        if not root:
            return
        res.append(root.val)
        self.traverse1(root.right)
        self.traverse1(root.left)
        return res

from queue import PriorityQueue

a = [1,2]
print(a.pop())