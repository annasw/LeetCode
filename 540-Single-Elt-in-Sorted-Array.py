# ok, leetcode is genuinely hard to deal with sometimes
# also python string slicing is pretty awful

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1: return nums[0]
        mid = (len(nums)-1)/2 # index of median elt
        numPairs = mid # same number; number of pairs
        if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        elif nums[mid]==nums[mid-1]:
            if numPairs%2!=0:
                return self.singleNonDuplicate(nums[mid+1:])
            else: #numpairs is even
                return self.singleNonDuplicate(nums[:mid-1])
        else: # nums[mid]==nums[mid+1]
            if numPairs%2!=0:
                return self.singleNonDuplicate(nums[:mid])
            else:
                return self.singleNonDuplicate(nums[mid+2:])
        
        
