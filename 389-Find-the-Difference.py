class Solution:
    def findTheDifference(self, s: 'str', t: 'str') -> 'str':
        # once more hash tables save the day
        
        if len(s) == 0: return t[0]
        
        sDict = {}
        tDict = {}
        for i in s:
            sDict[i] = sDict.get(i,0) +1
        for i in t:
            tDict[i] = tDict.get(i,0) +1
            
        for a in tDict:
            if sDict.get(a,0) != tDict[a]:
                return a
        
        return # we shouldn't ever get to this point
