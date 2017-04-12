class Solution(object):
    def reverseVowels(self,s):
        vowels = set(list('aeiouAEIOU'))
        
        if len(s)<2: return s
        
        s = list(s)
        
        left = 0
        right = len(s)-1
        while left<right:
            while left<right and s[left] not in vowels:
                left += 1
            while right>left and s[right] not in vowels:
                right -= 1
            if left != right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
            left += 1
            right -= 1
        return ''.join(s)
    
    # Old, slower method -- works, but a little slow
    '''def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        newString = ''
        if not s: return s
        vowelIndex = len(s)
        
        for char in s:
            if char not in vowels: # consonant
                newString = newString + char
            else: # vowel
                for idx in xrange(vowelIndex-1,-1,-1):
                    if s[idx] in vowels:
                        newString = newString + s[idx]
                        vowelIndex = idx
                        break
        return newString'''
        
