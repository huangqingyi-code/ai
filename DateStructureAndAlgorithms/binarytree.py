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

class Node:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            lst = [self.root]
            while lst:
                root = lst.pop(0)
                if root.left == None:
                    root.left = node
                    break
                else:
                    lst.append(root.left)
                if root.right == None:
                    root.right = node
                    break
                else:
                    lst.append(root.right)
    # def sorted_add(self,item):
    #     node = Node(item)
    #     if self.root == None:
    #         self.root = node
    #         return
    #     else:
    #         lst = [self.root]
    #         while lst:
    #             root = lst.pop(0)
    #             if root.item > node.item:
    #                 if root.left == None:
    #                     root.left = node
    #                     return
    #                 else:
    #                     lst.append(root.left)
    #             else:
    #                 if root.right == None:
    #                     root.right = node
    #                     return
    #                 else:
    #                     lst.append(root.right)
    def sorted_add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        else:
            cur = self.root
            while cur:
                if item < cur.item:
                    if cur.left == None:
                        cur.left = node
                        return
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = node
                        return
                    else:
                        cur = cur.right
    def breadth_first(self):
        if self.root == None:
            return
        else:
            lst = [self.root]
            while lst:
                root = lst.pop(0)
                print(root.item)
                if root.left:
                    lst.append(root.left)
                if root.right:
                    lst.append(root.right)
    def forward(self,root):
        if root == None:
            return
        else:
            print(root.item)
            self.forward(root.left)
            self.forward(root.right)
    def middle(self,root):
        if root == None:
            return
        else:
            self.middle(root.left)
            print(root.item)
            self.middle(root.right)
    # def middle(self,root):
    #     if root == None:
    #         print('')
    #     else:
    #         self.middle(root.left)
    #         print(root.item,end='')
    #         self.middle(root.right)
tree = Tree()
# tree.add(1)
# tree.add(2)
# tree.add(3)
# tree.add(4)
# tree.add(5)
# tree.add(6)
# tree.add(7)
# tree.breadth_first()
# tree.forward(tree.root)
# tree.middle(tree.root)
tree.sorted_add(5)
tree.sorted_add(12)
tree.sorted_add(3)
tree.sorted_add(1)
tree.sorted_add(8)
tree.sorted_add(6)
tree.sorted_add(4)
tree.sorted_add(2)
tree.middle(tree.root)