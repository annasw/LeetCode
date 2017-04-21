class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # naive O(n**2) solution
        '''maxProduct = nums[0]
        for i in range(len(nums)):
            localProduct = 1
            for j in range(i,len(nums)):
                localProduct *= nums[j]
                maxProduct = max(maxProduct, localProduct)
        return maxProduct'''
        
        # less naive solution
        grandMax = smallest = biggest = nums[0]
        for n in nums[1:]:
            smallest, biggest = min(n, smallest*n, biggest*n), max(n, smallest*n, biggest*n)
            grandMax = max(grandMax, biggest)
        return grandMax
        
