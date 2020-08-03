# 1. 二叉树的前序遍历

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
        if not self.root:
            self.root = node
        else:
            lst = [self.root]
            while lst:
                root = lst.pop(0)
                if root.left == None:
                    root.left = node
                    break
                else:lst.append(root.left)
                if root.right ==None:
                    root.right = node
                    break
                else:lst.append(root.right)
    #递归
    def preorder_recusion(self,root):
        if not root:
            return
        else:
            # print(root.item)
            self.preorder_recusion(root.left)
            # print(root.item)
            self.preorder_recusion(root.right)
            print(root.item)

    #前序非递归方法一
    def preorder_norecusion1(self,root):
        if not root:
            return []
        stack,res = [root],[]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.item)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
    # 前序非递归方法2
    def preorder_norecusion2(self,root):
        if not root:
            return []
        cur,stack,res = root,[],[]
        while cur or stack:
            while cur:
                res.append(cur.item)
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            cur = temp.right
        return res
    # 中序非递归方法
    def inorder_norecursion(self,root):
        if not root:
            return []
        cur,stack,res = root,[],[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            res.append(temp.item)
            cur = temp.right
        return res
    #后序非递归方法1
    def postorder_norecursion1(self,root):
        if not root:
            return []
        cur,stack,res = root,[],[]
        while cur or stack:
            while cur:
                res.append(cur.item)
                stack.append(cur)
                cur = cur.right
            temp = stack.pop()
            cur = temp.left
        return res[::-1]
    # 后序非递归方法2
    def postorder_norecursion2(self,root):
        if not root:
            return []
        stack,res = [(0,root)],[]
        while stack:
            flag,node = stack.pop()
            if not node:continue
            if flag==1:#遍历过了加入到结果
                res.append(node.item)
            else:
                stack.append((1,node))
                stack.append((0,node.right))
                stack.append((0,node.left))
        return res

tree = Tree()
tree.add(6)
tree.add(5)
tree.add(7)
tree.add(8)
tree.add(4)
tree.add(3)
tree.add(9)
# tree.preorder_recusion(tree.root)
# ret2 = tree.postorder_norecursion2(tree.root)
# ret1 = tree.postorder_norecursion1(tree.root)
# print(ret1,ret2)
