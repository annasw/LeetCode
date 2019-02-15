class Solution:
# this problem was rated Medium
# this solution is faster than 100% of submissions
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        return sorted(nums)[-k]
