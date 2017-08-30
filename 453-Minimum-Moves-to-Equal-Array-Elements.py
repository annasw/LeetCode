class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is way easier to think about as decrementing one number
        # and obviously you just decrement each number to the min number in turn
        
        minElt = min(nums)
        return sum([n-minElt for n in nums])
        
        # one-liner that works, but too slowly, b/c min(nums) is O(n)
        # return sum([n-min(nums) for n in nums])
        
