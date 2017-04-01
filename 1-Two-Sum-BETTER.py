'''
So my "old" leetcode acct is gone
(which is actually fine and part of the reason why i have this github)
but i'm gonna try to improve on my old solutions anyway.
(Slash practice so I remember them better.)
This is an improvement ot my old Two-Sum solution.
That one ran in O(n^2);
This one runs in O(n).
Thanks, hashtables (and better algorithms skills)!
Of course that one technically ran in constant space,
but let's be real: unless otherwise specified, time>space.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {} # keys=numbers, values=indices
        for idx in range(len(nums)):
            num = nums[idx]
            diff = target-num
            if diff in d:
                ans = []
                ans.append(d[diff])
                ans.append(idx)
                return ans
            else:
                d[num] = idx
