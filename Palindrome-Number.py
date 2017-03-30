class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        s = str(x)
        if len(s)==0:
            return True
        left = 0
        right = len(s)-1
        while left!=right and left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        
        return True
        
