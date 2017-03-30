class Solution(object):
    import string
    def myAtoi(self, st):
        """
        :type st: String
        :rtype: int
        """
        
        s = ''.join(st.strip())
        
        result = 0
        negative = False
        
        if len(s)>=2:
            if s[0]=='+':
                s = s[1:]
            elif s[0]=='-':
                negative = True
                s = s[1:]
        
        try:
            while s:
                if s[0] in string.whitespace:
                    break
                result = int(str(result) + s[0])
                s = s[1:]
        
        except ValueError:
            pass
            #if negative: result = -1*result
            #return result
        
        if negative: result = -1*result
        if result>2147483647:
            result = 2147483647
        elif result<-2147483648:
            result = -2147483648
        return result
    
