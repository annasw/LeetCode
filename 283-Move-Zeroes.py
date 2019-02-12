class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0: zeroes.append(i)
        
        numRemoved = 0
        for i in zeroes:
            nums.pop(i-numRemoved) # ugh accounting for index movement
            nums.append(0)
            numRemoved += 1
