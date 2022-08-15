# 二叉树的序列化和反序列化

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(self, root):

    if not root:return "null,"
    left=self.serialize(root.left)
    right=self.serialize(root.right)
    return str(root.val)+','+left+right
    

def deserialize(self, data):

    data=data.split(',')
    root=self.helper(data)
    return root

def helper(self,data):

    val=data.pop(0)
    if val=='null':return None
    node=TreeNode(val)
    node.left=self.helper(data)
    node.right=self.helper(data)
    return node

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

codec = Codec()
print(codec.serialize(node1))
print(codec.deserialize(codec.serialize(node1)).left)