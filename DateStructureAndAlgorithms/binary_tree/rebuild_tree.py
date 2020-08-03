class TreeNode:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
class Solution:
    def rebuild_binarytree(self,pre,inorder):
        if not pre:
            return
        index = inorder.index(pre[0])
        node = TreeNode(inorder[index])

        node.left = self.rebuild_binarytree(pre[1:index+1],inorder[:index])
        node.right = self.rebuild_binarytree(pre[index+1:],inorder[index+1:])
        return node