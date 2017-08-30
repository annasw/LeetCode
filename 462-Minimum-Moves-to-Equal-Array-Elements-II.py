class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # the median number will always work (either median if it's even-length)
        
        pivot = sorted(nums)[int(len(nums)/2)]
        return sum([abs(pivot-i) for i in nums])
        
