class Solution:
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        if len(secret) == 0: return ''
                
        bullCount = 0
        
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bullCount += 1
        
        # make dicts w/out bulls
        secList = [secret[i] for i in range(len(secret)) if not secret[i] == guess[i]]
        gueList = [guess[i] for i in range(len(guess)) if not secret[i] == guess[i]]
                
        s = {}
        g = {}
        for e in secList:
            s[e] = s.get(e,0) +1
        for e in gueList:
            g[e] = g.get(e,0) +1
        
        # count cows
        cowCount = 0
        for e in s:
            cowCount += min(s[e], g.get(e,0))
        
        # oh and before we finish can i say that i resent that A is for Abulls and B is for Bcows.
        # AS SOMEONE WHO STUDIED THE ALPHABET IN SCHOOL
        return "" + str(bullCount) + 'A' + str(cowCount) + 'B'
