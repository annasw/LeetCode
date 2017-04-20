class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # first determine if there is a third-largest
        if len(set(nums))<3:
            return max(nums) # just return the largest number
        
        first, second, third = min(nums),min(nums),min(nums)
        for i in nums:
            if i>first:
                first,second,third = i,first,second
            elif i>second and i!=first:
                second,third = i,second
            elif i>third and i!=second and i!=first:
                third = i
        return third
        
