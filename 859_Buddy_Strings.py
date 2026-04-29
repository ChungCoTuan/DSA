class Solution:
    def buddyStrings(self, s, goal):
        # Điều kiện đầu tiên: Độ dài phải bằng nhau
        if len(s) != len(goal):
            return False
            
        # Trường hợp 1: Hai chuỗi giống hệt nhau
        if s == goal:
            # Ta chỉ có thể tráo đổi nếu có ít nhất một ký tự xuất hiện 2 lần
            # Ví dụ: "aba" -> tráo hai chữ 'a' vẫn là "aba" (True)
            # Ví dụ: "abc" -> tráo bất kỳ cũng làm chuỗi khác đi (False)
            unique_chars = set(s)
            return len(unique_chars) < len(s)
            
        # Trường hợp 2: Hai chuỗi khác nhau
        # Tìm tất cả các vị trí mà tại đó s[i] != goal[i]
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                
        # Để là "Buddy Strings", phải có đúng 2 vị trí khác biệt
        if len(diff) == 2:
            i, j = diff
            # Và ký tự tại hai vị trí đó phải chéo nhau
            # s = "ab", goal = "ba" -> s[0]==goal[1] và s[1]==goal[0]
            return s[i] == goal[j] and s[j] == goal[i]
            
        # Các trường hợp còn lại (0, 1 hoặc > 2 vị trí khác biệt) đều False
        return False