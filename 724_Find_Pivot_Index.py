class Solution:
    def pivotIndex(self, nums):
        # Tính tổng của toàn bộ mảng
        total_sum = sum(nums)
        # Biến lưu tổng các số bên trái của chỉ số hiện tại
        left_sum = 0
        
        for i, x in enumerate(nums):
            # Tổng bên phải sẽ bằng: Tổng toàn bộ - Tổng bên trái - Giá trị hiện tại
            # Công thức cân bằng: left_sum == (total_sum - left_sum - x)
            if left_sum == total_sum - left_sum - x:
                return i
            
            # Cập nhật tổng bên trái để chuẩn bị cho bước tiếp theo
            left_sum += x
            
        return -1