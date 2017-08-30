class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x==0: return 0
        if x<0: return 0 #huh
        
        # we use the Babylonian method
        # 1000 iterations is massive overkill -- in my testing it works perfectly w/ 100 -- but
        # leetcode was irritating me and i wanted to make sure i could handle outrageous trials
        
        guess = x
        for iteration in range(0,1000):
            guess = .5*(guess+x/guess)
        
        return int(guess)
        
