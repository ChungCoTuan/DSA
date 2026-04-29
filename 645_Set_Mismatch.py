class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        # Tổng lý thuyết từ 1 đến n
        expected_sum = n * (n + 1) / 2
        
        # Tổng thực tế của mảng
        actual_sum = sum(nums)
        
        # Tổng các phần tử không trùng lặp
        # set() vẫn tồn tại trong Python 2.x
        unique_sum = sum(set(nums))
        
        # Tính toán kết quả
        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum
        
        return [duplicate, missing]