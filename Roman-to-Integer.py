# doesn't actually work yet
# because i just coded this and i don't feel like coding it again
# but here's what i have

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        total = 0
        while s and s[0]=='M':
            total+=1000
            s=s[1:]
        while s and s[0]=='D':
            total+=500
            s=s[1:]
        while s and s[0]=='C':
            if len(s)>1:
                if s[1]==M:
                    total += 900
                if s[1]==D:
                    total += 400
            else:
                total += 100
            s = s[1:]
        while s and s[0]=='L':
            total += 50
