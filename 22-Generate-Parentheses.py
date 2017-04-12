class Solution(object):
    '''
    takes:
        n (number of PAIRS of parens),
        openPs (number of open parens so far),
        closePs (number of close parens so far),
        and fragment (to track the current string fragment).
    '''
    def recursiveParens(self, n, openPs, closePs, fragment):
        if len(fragment) == n*2: # the list is full
            return [fragment]

        results = []
        if openPs < n:
            lsOpen = self.recursiveParens(n, openPs+1, closePs, fragment+'(')
            for i in lsOpen: results.append(i)
        if closePs < n and closePs < openPs:
            lsClose = self.recursiveParens(n, openPs, closePs+1, fragment+')')
            for i in lsClose: results.append(i)
        
        return results
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0: return ''
        
        return self.recursiveParens(n, 0, 0, '')
        
