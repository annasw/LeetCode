'''
Problem: Implement atoi (a function in C/++). Do all research yourself. Deliberately vague.
Reference: C++ documentation for atoi function.
I missed uncommonly many test cases for this one (although it's done now). I'll comment them ALL in.
'''
class Solution(object):
    import string
    def myAtoi(self, st):
        """
        :type st: String
        :rtype: int
        """
        
        # CASE: used to split(' '), which is wrong -- internal whitespace should throw an exception
        # n.b. i used to have the join() method here, but it's not necessary w/out split().
        # oh speaking of which, CASE, I also didn't remember that string.join() returns a new string,
        # rather than replacing the original string
        s = st.strip()
        
        result = 0
        negative = False
        
        if len(s)>=2:
            if s[0]=='+':
                s = s[1:]
            # CASE: initially had another if here. they hit me with something like "+-6". that one was clever
            elif s[0]=='-':
                negative = True
                s = s[1:]
        
        try:
            while s:
                # CASE: i figured int(" ") would throw a ValueError; it doesn't. it just returns 0.
                if s[0] in string.whitespace:
                    break
                result = int(str(result) + s[0])
                s = s[1:]
        
        except ValueError:
            pass
        
        if negative: result = -1*result
        # CASE: the c++ documentation literally doesn't even deal with this, but i had to. i don't blame myself for this one.
        if result>2147483647:
            result = 2147483647
        elif result<-2147483648:
            result = -2147483648
        return result
