import sys,time,os

class Node():
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
            while self.root:
                if self.root.item>item:
                    if self.root.left == None:
                        self.root.left = node
                        return
                    else:self.root = self.root.left
                else:
                    if self.root.right == None:
                        self.root.right = node
                        return
                    else:self.root = self.root.right
    # def travel(self):
    #     if self.root == None:
    #         return
    #     else:
    #         lst = [self.root]
    #         while lst:
    #             root = lst.pop(0)
    #             if root.left:
    #                 lst.append(root)
    #             else:print(root.item)
    def inorder(self,root):
        if not root:
            return
        else:
            self.inorder(root.left)
            print(root.item)
            self.inorder(root.right)

tree = Tree()
tree.add(5)
tree.add(6)
tree.add(4)
tree.add(3)
tree.add(2)
tree.add(7)
tree.add(8)
tree.inorder(tree.root)