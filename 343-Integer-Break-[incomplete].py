class Solution(object):
    from math import *
    
    # takes integers f(loor), c(eiling), and goal
    # 
    def solver(f, c, goal):
        if goal%f==0:
            return
    
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2: return 1
        if n==3: return 2
        
        root = sqrt(n)
        if int(root)==root:
            return root**root
        else:
            f = floor(root)
            c = ceil(root)
            
            
