class Solution:
    def rotateString(self, s, goal):
        # Bước 1: Kiểm tra độ dài, nếu khác nhau thì chắc chắn không xoay được
        if len(s) != len(goal):
            return False
            
        # Bước 2: Kiểm tra xem goal có nằm trong s + s không
        return goal in (s + s)