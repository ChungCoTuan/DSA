class Solution:
    def judgeCircle(self, moves):
        # Đếm số lần xuất hiện của từng ký tự trong chuỗi moves
        # Robot về gốc nếu Up = Down và Left = Right
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')