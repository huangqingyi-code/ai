class TreeNode:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None
class Solution1:
    def binary_maxdepth(self,root,depth):
        if not root:
            return depth
        if depth==0:
            return 0
        left_depth = self.binary_maxdepth(root.left,depth+1)
        right_depth = self.binary_maxdepth(root.right,depth+1)
        return max(left_depth,right_depth)

class Solution2:
    def binary_maxdepth(self,root):
        if not root:
            return 0
        lst = [root]
        depth = 0
        while lst:
            num = len(lst)
            for i in range(num):
                root = lst.pop(0)
                if root.left:
                    lst.append(root.left)
                if root.right:
                    lst.append(root.right)
            depth+=1
        return depth


