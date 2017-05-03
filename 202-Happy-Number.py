class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        sums = set([])
        
        while True:
            sum = 0
            for digit in str(n):
                sum += int(digit)**2
            if sum == 1: return True
            if sum in sums: return False
            sums.add(sum)
            n = sum
            
