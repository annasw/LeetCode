# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==q==[] or p==q==None: return True
        elif p==[] or q==[] or p==None or q==None: return False
        
        # a lot of this is unnecessary and can be cleaned up, but it works and isn't inefficient
        if p.val!=q.val: return False
        if (p.left==None and q.left!=None) or (p.left!=None and q.left==None): return False
        elif p.left!=None and q.left!=None: # both have a left child
            if not self.isSameTree(p.left,q.left): return False
        if (p.right==None and q.right!=None) or (p.right!=None and q.right==None): return False
        elif p.right!=None and q.right!=None: #both have right child
            if not self.isSameTree(p.right,q.right): return False
        return True
        
