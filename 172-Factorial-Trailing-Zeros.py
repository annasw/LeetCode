class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # The key here is to notice that the number of trailing zeros
        # depends entirely on the number of 10s multiplied into the factorial,
        # which in turn depends on the number of 5s multiplied in.
        # But for greater powers of 5 we need to count multiple times,
        # So we recount for each power of 5 until 5**power > n.
        numZeros = 0
        power = 1
        div = n//(5**power)
        while div!=0:
            numZeros += div
            power += 1
            div = n//(5**power)
        return numZeros
        
