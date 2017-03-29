class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for x in range(0,length):
            for y in range(x+1,length):
                if nums[x]+nums[y]==target:
                    return [x,y]
        # this website is badly designed
        # which is a little (but not extremely) ironic
        
