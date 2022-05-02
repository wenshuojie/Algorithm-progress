# 297. 二叉树的序列化与反序列化
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

################ 前序遍历 start################

    def serialize(self, root):
        char = ''
        def Helper(root):
            nonlocal char # nolocal的用法
            if not root:
                char += '#,'
                return

            char += str(root.val)+','
            Helper(root.left)
            Helper(root.right)

        Helper(root)
        return char
        

    def deserialize(self, data):
        data = deque(data.split(',')) # 要使用popleft()，需要转化为deque对象
        return self.deserialize_ass(data)

    def deserialize_ass(self,data):
        if not data:
            return

        root_val = data.popleft()
        if root_val == '#':
            return None
        root = TreeNode(root_val)
        root.left = self.deserialize_ass(data)
        root.right = self.deserialize_ass(data)

        return root

################ 前序遍历 end################
