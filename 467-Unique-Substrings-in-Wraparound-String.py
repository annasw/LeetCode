class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if len(p)==0: return 0
        if len(p)==1: return 1
        # so alphaString.find(x)+1 will return the expected next character (or 0 if n/a)
        alphaString = 'zabcdefghijklmnopqrstuvwxyz'
        subStringSet = set([]) # only used in my naive implementation
        headPointer = 0
        tailPointer = 0
        
        '''Original, naive implementation -- timed out. O(n**2)'''
        # have two pointers: one at beginning of substring, one at end
        # add substring to hashset starting at one character
        # if the next character is the expected next character, increment tail
        # if not, increment head and set tail to head+1
        # do this while tail < len(p)
        # then return the size of the hashset
        '''while tailPointer < len(p):
            # assume at the start that we have a valid substring
            subStringSet.add(p[headPointer:tailPointer+1])
            # now check the next character (note that "substring in alphaString" fails for longer substrings)
            if tailPointer < len(p)-1 and p[tailPointer+1]==alphaString[alphaString.find(p[tailPointer])+1]:
                tailPointer += 1
            else:
                headPointer += 1
                tailPointer = headPointer
        return len(subStringSet)'''
        
        '''Second, better implementation -- worked. O(n).'''
        # Better solution:
        # Keep track, in a dict, of the longest substring we've seen starting at a given letter
        # Then the number of substrings starting with that letter is the length of the longest substring starting with that letter
        longestSubstring = {x:0 for x in alphaString[1:]}
        while tailPointer < len(p):
            if tailPointer < len(p)-1 and p[tailPointer+1]==alphaString[alphaString.find(p[tailPointer])+1]:
                tailPointer+=1
            else:
                longestSubstring[p[headPointer]] = max(longestSubstring.get(p[headPointer]),tailPointer-headPointer+1)
                headPointer+=1
                if tailPointer<headPointer: tailPointer = headPointer
        sum = 0
        for key in longestSubstring: sum += longestSubstring[key]
        return sum
        
        
