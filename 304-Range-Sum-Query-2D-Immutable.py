class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sumGrid = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        
        # given a sum square A B
        #                    C D
        # the sum at D is the sum at B+C-A plus the value at D in matrix.
        
        # make sure we're not trying to fill empty lists
        if len(self.sumGrid)==0 or len(self.sumGrid[0])==0:
            return
        
        # We start by filling the top row and left column to make it easy.
        self.sumGrid[0][0] = matrix[0][0]
        for col in range(1,len(matrix[0])):
            self.sumGrid[0][col] = self.sumGrid[0][col-1] + matrix[0][col]
        for row in range(1,len(matrix)):
            self.sumGrid[row][0] = self.sumGrid[row-1][0] + matrix[row][0]
        
        # now we fill the rest of the grid according to the above principle
        # (unless it's one-dimensional in which case we're already done)
        if len(matrix) > 1 and len(matrix[0]) > 1:
            for row in range(1, len(matrix)):
                for col in range(1, len(matrix[0])):
                    self.sumGrid[row][col] = self.sumGrid[row-1][col]+self.sumGrid[row][col-1]-self.sumGrid[row-1][col-1]+matrix[row][col]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # first check that we're not trying to return from an empty list
        if len(self.sumGrid)==0 or len(self.sumGrid[0])==0: return 0
        
        # The sum from square (row1, col1) to square (row2, col2) is
        # the sum at the bottom right square
        # minus the sum of the horizontal part above (i.e. (row1-1,col2) IF row1>0)
        # minus the sum of the vertical part to the left (i.e. (row2,col1-1) if col1>0)
        # plus the double-subtracted part ((row1-1,row2-1) if both row1>0 and row2>0.
        result = self.sumGrid[row2][col2]
        if row1>0: result -= self.sumGrid[row1-1][col2]
        if col1>0: result -= self.sumGrid[row2][col1-1]
        if row1>0 and col1>0: result += self.sumGrid[row1-1][col1-1]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
