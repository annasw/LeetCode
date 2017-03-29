class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        
        is_negative = x<0
        if is_negative: x = -1*x
        
        x_reversed = int(str(x)[::-1])
        if is_negative:
            x_reversed = -1*x_reversed
        # in my tests x_reversed got converted to a long and this code worked
        #if type(x_reversed)==long: return 0
        # here it stays an int so we can just check
        if x_reversed < -2147483648 or x_reversed>2147483647: return 0
        return x_reversed
