# Given a combination of numbers typed into an old-school cell phone,
# return all possible strings that combination of numbers could create.

class Solution(object):
    def generateWords(self, digits, fragment):
        results = []
        if len(digits)==1: # we're on the last digit
            for letter in self.correspondences[digits[0]]:
                results.append(fragment+letter)
            return results
        
        for letter in self.correspondences[digits[0]]:
            # results becomes a list of lists
            results.append(self.generateWords(digits[1:], fragment+letter))
        finalResults = []
        for ls in results:
            for i in ls:
                finalResults.append(i)
        return finalResults

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0: return []
        
        self.correspondences = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        return self.generateWords(digits, '')
