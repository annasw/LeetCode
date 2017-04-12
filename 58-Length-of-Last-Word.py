class Solution(object):
    # Split the string by whitespace (string.split() w/out args does this)
    # This leaves us with a list of words, if applicable
    # Then check if the list exists, and if so return the length of its last elt. If not, return 0.
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls = s.split()
        if not ls: return 0
        else: return len(ls[-1])
        
        # Old, worse solution, before I realized that string.split() w/out args splits along ALL whitespace:
        '''
        ls = s.split(' ')
        for i in range(len(ls)-1,-1,-1):
            if ls[i] != '': # it's a word
                return len(ls[i])
        return 0 # everything was whitespace
        '''
        
