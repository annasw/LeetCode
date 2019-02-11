class Solution:
    # runs in O(len(t)), aka linear time
    def isSubsequence(self, s: 'str', t: 'str') -> 'bool':
        if len(s)<1: return True
        if len(t)<1: return False
        
        char = s[0] # the first character we need to find in t
        for i in t:
            if char == i:
                s = s[1:]
                if len(s) < 1:
                    return True # we found all characters in s
                char = s[0] # new char we're searching for
        return False # we've reached the end of t and haven't found all characters in s
