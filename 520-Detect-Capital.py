import string

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<=1: return True # for 0- or 1-length words, any capitalization is fine
        
        if word[0] in string.ascii_lowercase: # all letters need to be lowercase
            for i in word:
                if i not in string.ascii_lowercase:
                    return False
            return True
        else: # word[0] is uppercase
            if word[1] in string.ascii_uppercase: # all letters must be uppercase
                for i in word:
                    if i not in string.ascii_uppercase:
                        return False
                return True
            else: # all remaining letters must be lowercase
                for i in word[1:]:
                    if i not in string.ascii_lowercase:
                        return False
                return True
        
