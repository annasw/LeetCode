class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letterSet = set([])
        for i in range(len(s)):
            if s[i] not in letterSet:
                if s[i] not in s[i+1:]:
                    return i
                else:
                    letterSet.add(s[i])
        return -1
        
