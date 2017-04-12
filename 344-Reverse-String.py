class Solution(object):
    # quick and trivial
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    
    # "slow" and manual (not actually slow, but probably slowER)
    def reverseString(self,s):
        if not s: return ''
        
        s = list(s)
        left = 0
        right = len(s)-1
        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return ''.join(s)
        
