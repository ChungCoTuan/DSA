class Solution:
    def selfDividingNumbers(self, left, right):
        res = []
        
        for num in range(left, right + 1):
            # Biến kiểm tra xem số hiện tại có thỏa mãn điều kiện không
            is_self_dividing = True
            
            # Chuyển số thành chuỗi để duyệt từng chữ số
            for char in str(num):
                digit = int(char)
                
                # Điều kiện 1: Không được chứa chữ số 0
                # Điều kiện 2: Số gốc phải chia hết cho chữ số đó
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break
            
            if is_self_dividing:
                res.append(num)
                
        return res