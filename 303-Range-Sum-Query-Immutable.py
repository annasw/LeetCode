class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumArray = [0 for i in range(len(nums))]
        
        if len(nums) == 0: return
        
        self.sumArray[0] = nums[0]
        for i in range(1,len(nums)):
            self.sumArray[i] = self.sumArray[i-1]+nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(self.sumArray)==0: return 0
        
        result = self.sumArray[j]
        if i>0: result -= self.sumArray[i-1]
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
