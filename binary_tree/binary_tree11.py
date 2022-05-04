# 297. 二叉树的序列化与反序列化
from collections import deque

from sklearn import tree #可两端操作

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

################ 前序遍历 start ################
class Codec_pre:
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
        return self.deserialize_help(data)

    def deserialize_help(self,data):
        if not data:
            return

        root_val = data.popleft() # 前序遍历，第一个元素是root
        if root_val == '#':
            return None
        root = TreeNode(root_val)
        root.left = self.deserialize_help(data)
        root.right = self.deserialize_help(data)

        return root
################ 前序遍历 end ###############


################ 后序遍历 start ###############
class Codec_post:
    def serialize(self, root):
        char = [] # 后序遍历，这里不能直接使用str，不然会出现形如：#,#,2,#,#,4,#,#,5,3,1,（最后一个是一个逗号）
        def serialize_help(root):
            nonlocal char
            if not root:
                char.append('#')
                return
            serialize_help(root.left)
            serialize_help(root.right)
            char.append(str(root.val))

        serialize_help(root)
        return ','.join(char)

    def deserialize(self,data):
        data = data.split(',')
        return self.deserialize_help(data)

    def deserialize_help(self,data):
        if not data:
            return

        root_val = data.pop() # 后序遍历，最后一个元素是root
        if root_val == '#':
            return
        root = TreeNode(root_val)
        root.right = self.deserialize_help(data) # 先构造右子树
        root.left = self.deserialize_help(data)
    
        return root
################ 后序遍历 end ###############

################ 层级遍历 start ###############
class Codec_level:
    def serialize(self, root):
        if not root:
            return '' # note
        
        char = []
        tree_queue = deque()
        tree_queue.append(root)
        while tree_queue:
            node = tree_queue.popleft()
            if not node: # 层级遍历，要还原需要空指针
                char.append('#')
                continue
            else:
                char.append(str(node.val))
            
            tree_queue.append(node.left)
            tree_queue.append(node.right)

        return ','.join(char)

    def deserialize(self, data):
        if not data:
            return

        data = data.split(',')
        tree_queue = deque() # 记录父节点
        root = TreeNode(int(data[0]))
        tree_queue.append(root)
        i = 1
        while i < len(data):
            parent = tree_queue.popleft()
            left_val = data[i]
            if left_val != '#':
                parent.left = TreeNode(int(left_val))
                tree_queue.append(parent.left)
            else:
                parent.left = None
            i += 1

            right_val = data[i]
            if right_val != '#':
                parent.right = TreeNode(int(right_val))
                tree_queue.append(parent.right)
            else:
                parent.right = None
            i += 1

        return root
################ 层级遍历 end ###############

        
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)

p1.left = p2
p1.right = p3
p3.left = p4
p3.right = p5

codec = Codec_level()
print(codec.serialize(None))


