class Solution:
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        
        min_row = float('inf')
        min_col = float('inf')
        
        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)
        
        return min_row * min_col