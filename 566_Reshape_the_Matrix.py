class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flat = []
        
        for row in mat:
            for val in row:
                flat.append(val)
        
        res = []
        
        for i in range(0, len(flat), c):
            res.append(flat[i:i+c])
        
        return res