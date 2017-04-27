# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathRecursive(self, root, sum, acc):
        acc += root.val
        if root.left==None and root.right==None:
            return acc == sum
        
        if root.left!=None:
            if self.hasPathRecursive(root.left, sum, acc):
                return True
        if root.right!=None:
            if self.hasPathRecursive(root.right, sum, acc):
                return True
        return False
    
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if root == None: return False
        return self.hasPathRecursive(root,sum,0)
        
