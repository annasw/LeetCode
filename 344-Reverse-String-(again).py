class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        
        for e in range (math.ceil(len(s)/2)):
            temp = s[e]
            s[e] = s[-(e+1)]
            s[-(e+1)] = temp
        
        # they changed the problem so now my beautiful easy solutions don't work
        #s = s[::-1] #s = [s[-(i+1)] for i in range(len(s))]
