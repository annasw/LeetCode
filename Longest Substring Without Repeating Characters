class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        currSequence = ''
        while s:
            # chop off the first character in the sequence, so 'abc' + 'ad' -> 'bcad'
            if s[0] in currSequence:
                currSequence = currSequence[1:]
            else:
                currSequence = currSequence + s[0]
                maxLength = max(maxLength, len(currSequence))
                s = s[1:]
        return maxLength
