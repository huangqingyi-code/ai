# 二叉树：
#      根节点
#      叶子节点：1.左叶子节点2.右叶子节点
#      树的层级
#      树的高度
# 二叉树遍历：1.广度优先遍历：一层一层遍历
#             2.深度优先遍历
#                  前序：根 左右
#                  中序：左跟右
#                  后序：左右根

class Node():
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
class Tree():
    def __init__(self):
        self.root = None
    def add_node(self,item):
        node = Node(item)
        if self.root==None:
            self.root = node
            return
        else:
            sequence = [self.root]
            while sequence:
                root = sequence.pop(0)
                if root.left == None:
                    root.left = node
                    break
                else:
                    sequence.append(root.left)
                if root.right == None:
                    root.right = node
                    break
                else:
                    sequence.append(root.right)
    def travel(self):
        if self.root == None:
            return ''
        else:
            sequence = [self.root]
            while sequence:
                root = sequence.pop(0)
                print(root.item)
                if root.left:
                    sequence.append(root.left)
                if root.right:
                    sequence.append(root.right)
    def add (self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        cur = self.root
        while True:
            if item > cur.item:
                if cur.right == None:
                    cur.right = node
                    return
                else:
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = node
                    return
                else:
                    cur = cur.left
    def middle_travel(self,root):
        if root == None:
            print('')
        else:
            self.middle_travel(root.left)
            print(root.item,end='')
            self.middle_travel(root.right)


tree = Tree()
tree.add(4)
tree.add(2)
tree.add(3)
tree.add(1)
tree.add(7)
tree.add(6)
tree.add(5)
tree.middle_travel(tree.root)





