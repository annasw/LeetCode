# I timed this one (a LeetCode medium): 18 minutes from first seeing the problem to full, working implementation
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        weights = [[0 for x in range(n)] for y in range(m)]
        # fill bottom-right square
        weights[m-1][n-1] = grid[m-1][n-1]
        # fill bottom row (we do this now to make our later work a little easier)
        for x in range(n-2, -1, -1):
            weights[m-1][x] = weights[m-1][x+1]+grid[m-1][x]
        # fill right column
        for y in range(m-2, -1, -1):
            weights[y][n-1] = weights[y+1][n-1]+grid[y][n-1]
        # fill rest of grid by rows, bot to top
        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                weights[row][col] = grid[row][col] + min(weights[row+1][col],weights[row][col+1])
        return weights[0][0]
        
