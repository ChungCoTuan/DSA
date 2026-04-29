class Solution:
    def floodFill(self, image, sr, sc, color):
        # Lấy màu gốc tại vị trí bắt đầu
        start_color = image[sr][sc]
        
        # Nếu màu mới trùng với màu gốc, không cần làm gì cả (tránh lặp vô tận)
        if start_color == color:
            return image
        
        rows = len(image)
        cols = len(image[0])
        
        def dfs(r, c):
            # Kiểm tra:
            # 1. Có nằm trong biên ma trận không?
            # 2. Ô hiện tại có cùng màu với ô bắt đầu không?
            if 0 <= r < rows and 0 <= c < cols and image[r][c] == start_color:
                # Đổi màu ô hiện tại
                image[r][c] = color
                
                # Lan tỏa sang 4 hướng: Lên, Xuống, Trái, Phải
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        # Bắt đầu thuật toán từ vị trí đề bài cho
        dfs(sr, sc)
        return image