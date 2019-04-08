class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # first we have to do some annoying string manip,
        # because this question is terrible.
        # we begin by removing the useless characters
        # and yes, this is how we do it.
        # PLEASE NOTE that we're having to replace these characters with whitespace
        # because the problem occasionally hands you e.g. "a,b" and expects you to read them
        # as two separate words...
        # it was this or regexes, you guys. seriously.
        p = paragraph.translate({ord(c): " " for c in "!?',;.'"})
        
        # we then convert the paragraph into a list of strings
        ls = p.split()
        
        # and then convert all strings to lower case...
        for idx in range(len(ls)):
            ls[idx] = ls[idx].lower()
        
        # and now finally we can get to work.
        
        # we populate a dict with key=word, value=frequency
        d = {}
        for i in ls:
            d[i] = d.get(i,0)+1
        
        # then remove the banned words
        for ban in banned:
            if ban in d:
                del d[ban]
        
        # and finally locate the most popular remaining word
        maxFreq = 0
        maxWord = ""
        for e in d:
            if d[e] > maxFreq:
                maxFreq = d[e]
                maxWord = e
        
        return maxWord
