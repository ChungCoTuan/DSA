class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        land = 0
        adjacent = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land += 1
                    
                    # kiểm tra ô bên dưới
                    if i + 1 < rows and grid[i + 1][j] == 1:
                        adjacent += 1
                    
                    # kiểm tra ô bên phải
                    if j + 1 < cols and grid[i][j + 1] == 1:
                        adjacent += 1
        
        return 4 * land - 2 * adjacent