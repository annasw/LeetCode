class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        newStr = [i.lower() for i in s if i in string.ascii_letters or i in string.digits]
        
        for i in range(len(newStr)):
            if newStr[i] != newStr[-(i+1)]:
                return False
        return True
