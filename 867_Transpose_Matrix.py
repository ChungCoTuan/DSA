class Solution:
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Tạo ma trận mới với kích thước ngược lại: cols x rows
        # Lưu ý: res[c][r] tương ứng với matrix[r][c]
        res = [[0] * rows for _ in range(cols)]
        
        for r in range(rows):
            for c in range(cols):
                res[c][r] = matrix[r][c]
                
        return res