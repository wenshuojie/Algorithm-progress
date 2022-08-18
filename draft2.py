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

depth = 0
maxdepth = 0

def traverse(root):
    global depth, maxdepth
    if not root:
        return 0

    depth += 1
    if not root.left and not root.right:
        maxdepth = max(depth, maxdepth)
    traverse(root.left)
    traverse(root.right)
    depth -= 1
    return maxdepth

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
print(traverse(node1))