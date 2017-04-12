class Solution(object):
    def reverseStr(self, s, k): # more like recurseStr, am i right
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= len(s): # reverse the whole thing
            return s[::-1]
        elif 2*k >= len(s): # i.e. k <= len(s) <= 2*k
            first = s[0:k]
            second = s[k:]
            return first[::-1]+second
        else: # len(s) > 2*k, so we have to do this recursively (well, we don't HAVE to. but we're going to).
            first = s[0:k]
            second = s[k:2*k]
            rest = self.reverseStr(s[2*k:],k)
            return first[::-1]+second+rest
        
