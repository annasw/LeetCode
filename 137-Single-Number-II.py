class Solution:
    # one minute; faster than 100% of submitted solutions
    # truly hash tables are broken
    def singleNumber(self, nums: 'List[int]') -> 'int':
        d = {}
        
        for i in nums:
            d[i] = d.get(i,0)+1
            
        for i in d:
            if d[i] == 1: return i
