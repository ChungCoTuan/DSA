import math

class Solution:
    def imageSmoother(self, img):
        # Lấy kích thước của ma trận
        rows = len(img)
        cols = len(img[0])
        
        # Tạo ma trận kết quả với cùng kích thước, khởi tạo bằng 0
        # Cách khởi tạo này an toàn cho mọi phiên bản Python
        res = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                total_sum = 0
                count = 0
                
                # Duyệt qua các ô xung quanh từ (r-1, c-1) đến (r+1, c+1)
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        # Kiểm tra xem ô (i, j) có nằm trong phạm vi ma trận không
                        if 0 <= i < rows and 0 <= j < cols:
                            total_sum += img[i][j]
                            count += 1
                
                # Tính giá trị trung bình và làm tròn xuống (floor)
                # Trong Python, phép chia // là chia lấy phần nguyên (tương đương floor)
                res[r][c] = total_sum // count
                
        return res