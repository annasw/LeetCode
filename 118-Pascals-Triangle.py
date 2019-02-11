class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':
        # solved several ways
        # un-comment in the one you want to use
        
        # using the same algorithm as for #119:
        '''if numRows <= 0: return []
        
        rows = [[1]]
        i = 1
        while i < numRows:
            row = [1]
            j = 1
            while j <= i/2: # first half of the list
                row.append(round(row[-1]*((i + 1 - j)/j)))
                j += 1
        
            # fill in the second half
            j -= 1
            if i%2==0: j -= 1 # check if we need to repeat the middle number

            while j>=0:
                row.append(row[j])
                j -= 1
            
            rows.append(row)
            i += 1
        
        return rows'''
        
        
        # the intended way (probably):
        # (i.e. by making the rows iteratively
        # using addition)
        
        '''if numRows <= 0: return []
        
        rows = [[1]]
        i = 1
        while i < numRows:
            row = [1]
            j = 1
            while j < i:
                row.append(rows[i-1][j-1]+rows[i-1][j])
                j += 1
            row.append(1)
            rows.append(row)
            i += 1
        return rows'''
        
        
        
