# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if root==None: return paths
        
        if root.left == None and root.right == None:
            paths.append(str(root.val))
        if root.left!=None:
            leftPaths = self.binaryTreePaths(root.left)
            for i in leftPaths:
                paths.append(str(root.val)+"->"+i)
        if root.right!=None:
            rightPaths = self.binaryTreePaths(root.right)
            for i in rightPaths:
                paths.append(str(root.val)+"->"+i)
        return paths
        
