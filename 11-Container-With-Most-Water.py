class Solution(object):
    def maxArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # two pointers: one at head of list, one at tail
        # keep a running int of maximum area, check every step of the way
        # each time, increment/decrement the smaller of the two pointers
        
        head = 0
        tail = len(heights)-1
        maximumArea = (tail-head)*min(heights[tail],heights[head])
        while head!=tail:
            if heights[head]>heights[tail]:
                tail -= 1
            else:
                head += 1
            maximumArea = max(maximumArea, (tail-head)*min(heights[tail],heights[head]))
        
        return maximumArea
        
