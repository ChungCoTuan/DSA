class Solution:
    def binaryGap(self, n):
        # Chuyển số n sang chuỗi nhị phân (bỏ qua tiền tố '0b')
        binary_str = bin(n)[2:]
        
        max_gap = 0
        last_position = -1
        
        # Duyệt qua từng ký tự và vị trí của nó trong chuỗi nhị phân
        for i, digit in enumerate(binary_str):
            if digit == '1':
                # Nếu đây không phải số 1 đầu tiên tìm thấy
                if last_position != -1:
                    # Tính khoảng cách và cập nhật max_gap
                    max_gap = max(max_gap, i - last_position)
                
                # Cập nhật vị trí của số 1 gần nhất
                last_position = i
                
        return max_gap