class Solution:
    def calPoints(self, operations):
        # Sử dụng một list như một stack để lưu trữ điểm số
        stack = []
        
        for op in operations:
            if op == "+":
                # Cộng tổng của hai điểm số hợp lệ gần nhất
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Nhân đôi điểm số hợp lệ gần nhất
                stack.append(stack[-1] * 2)
            elif op == "C":
                # Hủy bỏ điểm số hợp lệ gần nhất (pop khỏi stack)
                stack.pop()
            else:
                # Nếu là một số nguyên, chuyển đổi kiểu dữ liệu và thêm vào stack
                stack.append(int(op))
        
        # Tổng của tất cả các điểm số trong stack
        return sum(stack)