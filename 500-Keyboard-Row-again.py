class Solution:
    def findWords(self, words: 'List[str]') -> 'List[str]':
        row1 = set("QWERTYUIOPqwertyuiop")
        row2 = set("ASDFGHJKLasdfghjkl")
        row3 = set("ZXCVBNMzxcvbnm")
        
        results = []
        for w in words:
            wset = set(w)
            if wset.issubset(row1) or wset.issubset(row2) or wset.issubset(row3):
                results.append(w)
        
        return results
