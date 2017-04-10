'''Doesn't pass all the test cases (too slow) but theoretically works in all cases.'''

# Why is water in this question?? Who knows?
# Also the ONLY indicator that i'm supposed to find the area is the name of the method and the rtype. The question says nothing about this.
# "height" is a TERRIBLE variable name for a list of integers. i'll change it to heights.

# okay so the problem i solved makes the (i think reasonable) assumption that a container is formed by two full vertical lines.
# but apparently -- and again, this is never so much as hinted at in the problem description -- it can be formed by any segment of a longer line.
# In fact the description implies the exact opposite: "Find two lines, which together with x-axis forms a container... Note: You may not slant the container." 
# this is why i hate leetcode.

'''
class Solution(object):
    def maxArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # dict. keys = heights; values = list of all x-coords at that height.
        # if we have two or more, take the 0th elt and the len-1st elt, then compute area
        d = {}
        
        for idx in range(len(heights)):
            if heights[idx] in d:
                d[heights[idx]].append(idx)
            else:
                d[heights[idx]] = [idx]
        
        maxVolume = 0
        for key in d:
            if len(d[key])>1:
                maxVolume = max(maxVolume, (d[key][-1]-d[key][0])*key) # max of current max and the max container size at that height
        return maxVolume
'''

# We can do basically the same solution, except that any tower of height n can be added to the lists of all towers of heights <n (because they can form a container together, apparently).
class Solution(object):
    def maxArea(self, heights):
        d = {}
        h = [] # list of all heights. will be sorted. (used to make later operations slightly more efficient)
        
        # populate d's keys with every height present (values are empty lists)
        for i in heights:
            if i not in d:
                d[i] = []
                h.append(i)
        
        h = sorted(h)
        
        for idx in range(len(heights)):
            i = 0
            for i in range(len(h)):
                if h[i]>heights[idx]: # iterate through heights. will break when we hit a height > heights[idx]
                    break
                d[h[i]].append(idx)

        maxVolume = 0
        for key in d:
            if len(d[key]) > 1:
                maxVolume = max(maxVolume, (d[key][-1]-d[key][0])*key)
        return maxVolume








