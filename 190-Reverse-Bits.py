class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        resultString = ''
        for digit in range(32): # 32-bit number
            if 1&n==1: # n ends in a 1
                resultString = resultString+str(1)
            else:
                resultString = resultString+str(0)
            n >>= 1
        return int(resultString,2)
        
