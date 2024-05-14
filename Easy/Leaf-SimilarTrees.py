# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1=self.getLeaves(root1, [])
        leaves2=self.getLeaves(root2, [])
        print(leaves1)
        print(leaves2)
        if len(leaves1) != len(leaves2):
            return False
        for i in range(len(leaves1)):
            if leaves1[i] != leaves2[i]:
                return False
        return True
        
    def getLeaves(self, root, res):
        if root.left == None and root.right == None:
            res.append(root.val)
            return res
        if root.left == None:
            self.getLeaves(root.right, res)
        elif root.right == None:
            self.getLeaves(root.left, res)
        else:
            self.getLeaves(root.right, res)
            self.getLeaves(root.left, res)
        return res