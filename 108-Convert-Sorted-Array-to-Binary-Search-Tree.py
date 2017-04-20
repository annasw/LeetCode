# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if len(nums) == 0: return []
        
        # the root node is the middle value
        value = nums[len(nums)//2]
        root = TreeNode(value)
        
        # make child trees recursively
        if value != nums[0]: # if there IS a left
            root.left = self.sortedArrayToBST(nums[:len(nums)//2]) # pass in left half
        if value != nums[-1]: # if there is a right
            root.right = self.sortedArrayToBST(nums[(len(nums)//2)+1:]) # pass in right half
        
        return root
        
