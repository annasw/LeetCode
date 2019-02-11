class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.nums = nums
        
        # store the sum up through each index for easy reference
        self.sums = []
        
        tot = 0
        for i in self.nums:
            tot += i
            self.sums.append(tot)
        

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        if i == 0: return self.sums[j]
        return self.sums[j]-self.sums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
