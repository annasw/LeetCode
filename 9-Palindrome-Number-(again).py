class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        # so much cleaner than my last solution tbh
        x = str(x)
        if x[0]=='-': return False
        
        for i in range(len(x)):
            if x[i] != x[-(i+1)]:
                return False
        
        return True
