# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # check edge cases (shouldn't happen)
        if not root or not p or not q: return []
        
        # check if both p and q are on the same side
        if p.val>root.val and q.val>root.val: return self.lowestCommonAncestor(root.right,p,q)
        if p.val<root.val and q.val<root.val: return self.lowestCommonAncestor(root.left,p,q)
        # otherwise (different sides or one of p or q is root) just return root
        else: return root
        
