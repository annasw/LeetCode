class Solution:
    # runs very fast
    # but uses like a huge amount of space
    # not sure why
    # possibly/probably something weird w/ leetcode
    def getRow(self, rowIndex: 'int') -> 'List[int]':
        # so this exists
        # https://en.wikipedia.org/wiki/Pascal%27s_triangle#Calculating_a_row_or_diagonal_by_itself
        
        row = []
        
        if rowIndex < 0: return row # i guess
        
        row.append(1)
        if rowIndex == 0: return row
        
        i = 1
        while i <= rowIndex/2: # first half of the list
            # please note that here we use round() instead of int()
            # because python computes 330*1.4 as 461.99999999999994 instead of 462
            # and i was failing a test case (rowIndex = 11)
            # lol
            # (but round() is better anyway)
            row.append(round(row[-1]*((rowIndex + 1 - i)/i)))
            i += 1
        
        # fill in the second half
        i -= 1
        if rowIndex%2==0: i -= 1 # check if we need to repeat the middle number
        
        while i>=0:
            row.append(row[i])
            i -= 1
        
        return row
        
        
