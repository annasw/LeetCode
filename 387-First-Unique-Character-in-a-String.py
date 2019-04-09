class Solution:
    def firstUniqChar(self, s: str) -> int:
        # there are a bunch of trivial solutions to this
        # trivial O(n**2) solution: just iterate thru it lol
        # trivial O(n**2) solution: list comp w/ basically the same principle
        # trivial O(n)/O(n) solution: make a dict lol
        # i'm guessing the dream is O(n)/O(1), as always, but (as i mentioned in the last entry)
        # i'm very tired and going with the O(n)/O(n) because n**2 is a big number kk
        
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        
        for idx in range(len(s)):
            if d[s[idx]] == 1:
                return idx
        
        return -1
