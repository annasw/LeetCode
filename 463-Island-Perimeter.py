class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # check empty grid
        if len(grid)==0: return 0
        
        perimeter = 0
        
        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[0])):
                if grid[rowIndex][colIndex]==1: # if it's a one (else do nothing)
                    if rowIndex==0 or grid[rowIndex-1][colIndex]==0: # top row
                        perimeter += 1
                    if colIndex==0 or grid[rowIndex][colIndex-1]==0: # leftmost col
                        perimeter += 1
                    if rowIndex==len(grid)-1 or grid[rowIndex+1][colIndex]==0: # bottommost row
                        perimeter += 1
                    if colIndex == len(grid[0])-1 or grid[rowIndex][colIndex+1]==0: # rightmost col
                        perimeter += 1
        return perimeter
