class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Tìm chỉ số ở giữa (dùng // để chia lấy nguyên trong Python)
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Nếu target lớn hơn, tìm ở nửa bên phải
                left = mid + 1
            else:
                # Nếu target nhỏ hơn, tìm ở nửa bên trái
                right = mid - 1
                
        # Nếu thoát vòng lặp mà không tìm thấy
        return -1