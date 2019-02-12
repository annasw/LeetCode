class Solution:
    def isHappy(self, n: 'int') -> 'bool':
        if n < 1: return False
        
        nums = {} # store the numbers we iterate through
        
        while n > 1:
            if n in nums: return False
            nums[n] = 0
            newN = 0
            for i in str(n):
                newN += int(i)**2
            n = newN
        
        return True
