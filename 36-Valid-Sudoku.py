class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # verify each row
        for row in board:
            values = []
            for elt in row:
                if elt != '.':
                    if elt in values:
                        return False
                    else:
                        values.append(elt)
                        
        # verify each column
        for colIdx in range(len(board[0])): # should be constant, but this is more modular
            values = []
            for row in board:
                val = row[colIdx]
                if val != '.':
                    if val in values:
                        return False
                    else:
                        values.append(val)
                        
        # verify each 3x3 square (this one won't be modular)
        for rowStartIdx in [0,3,6]:
            for colStartIdx in [0,3,6]:
                values = []
                for rowIdx in range(rowStartIdx, rowStartIdx+3):
                    for colIdx in range(colStartIdx, colStartIdx+3):
                        val = board[rowIdx][colIdx]
                        if val != '.':
                            if val in values:
                                return False
                            else:
                                values.append(val)
        # with all checks done, board must be valid
        return True
        
