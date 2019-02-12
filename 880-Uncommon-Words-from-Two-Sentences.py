class Solution:
    def uncommonFromSentences(self, A: 'str', B: 'str') -> 'List[str]':
        # hash tables are broken
        # i wrote this in four minutes and it runs as fast as anything and outright faster than 93% of submissions

        d = {}
        alist = A.split()
        blist = B.split()
        for word in alist+blist:
            d[word] = d.get(word,0) + 1
        
        return [x for x in d if d[x]==1]
