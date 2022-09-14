class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        if not root:
            return '#,'
        left = self.Serialize(root.left)
        right = self.Serialize(root.right)
        return str(root.val) + ',' + left + right

    def Deserialize(self, s):
        node_list = s.split(',')
        self.helper(node_list)

    def helper(self, node_list):
        val = node_list.pop(0)
        if val == '#':
            return
        node = TreeNode(val)
        node.left = self.helper(node_list)
        node.right = self.helper(node_list)

p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)

p1.left = p2
p1.right = p3
p3.left = p4
p3.right = p5

solution = Solution()
print(print(solution.Serialize(p1)))