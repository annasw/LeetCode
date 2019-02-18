class Solution:
    def isPowerOfFour(self, num: 'int') -> 'bool':
        if num < 1: return False
        while num % 4 == 0: num /= 4
        return num == 1
