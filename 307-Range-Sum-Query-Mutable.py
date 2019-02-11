class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.nums = nums
        
        self.sums = []
        
        tot = 0
        for i in self.nums:
            tot += i
            self.sums.append(tot)

    def update(self, i: 'int', val: 'int') -> 'None':
        oldVal = self.nums[i]
        self.nums[i] = val
        
        # having to update in O(n) is by far the biggest time-waste here
        for j in range(i, len(self.nums)):
            self.sums[j] += val - oldVal

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        if i == 0: return self.sums[j]
        return self.sums[j]-self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
