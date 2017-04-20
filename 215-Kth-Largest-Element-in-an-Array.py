class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # i misread the problem; this is a beautiful solution to a better problem
        #return sorted(list(set(nums)))[::-1][k-1]
        
        # this is a slightly-less-beautiful solution to the real problem
        return sorted(nums)[::-1][k-1]
        
