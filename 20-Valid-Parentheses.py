class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s: return True
        
        # stack whose top elt is the expected closing bracket for the last open bracket
        expectations = []
        for char in s:
            if char in ['[','(','{']:
                if char == '[':
                    expectations.append(']')
                elif char == '(':
                    expectations.append(')')
                elif char == '{':
                    expectations.append('}')
            else: # char is a closing bracket of some kind
                # if the stack is empty, we have a mismatch. if not, compare
                if not expectations or char != expectations[-1]:
                    return False
                else:
                    expectations = expectations[:-1]
        # at the end, we make sure the stack is empty (if not we have a mismatch)
        return not expectations
