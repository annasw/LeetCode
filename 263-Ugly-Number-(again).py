class Solution:
    # this time, it's recursive...
    def isUgly(self, num: 'int') -> 'bool':
        if num <= 0: return False
        if num in [1,2,3,5]: return True
        if num%2==0: return self.isUgly(num//2)
        if num%3==0: return self.isUgly(num//3)
        if num%5==0: return self.isUgly(num//5)
        return False # not divisible by 2, 3, or 5, therefore not ugly
        
