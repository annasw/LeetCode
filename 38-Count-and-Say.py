class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        
        s = '1' # the actual sequence
        
        for i in range(n-1): # to generate nth sequence -- we already did the first one
        
            # Does one run-through of See-And-Say
            seeAndSay = '' # the seeAndSay for the current iteration of s
            while s: # while we haven't iterated all the way through the number
                digit = s[0]
                digitCount = 0
                while s and s[0]==digit:
                    digitCount += 1
                    s = s[1:]
                seeAndSay = seeAndSay + str(digitCount)
                seeAndSay = seeAndSay + str(digit)
            
            s = seeAndSay
        
        return s
        
