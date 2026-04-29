class Solution:
    def countBinarySubstrings(self, s):
        # Mảng lưu độ dài của các nhóm ký tự giống nhau liên tiếp
        groups = []
        if not s:
            return 0
        
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count) # Thêm nhóm cuối cùng
        
        ans = 0
        # Tính tổng các giá trị tối thiểu của từng cặp cạnh nhau
        for i in range(1, len(groups)):
            ans += min(groups[i], groups[i-1])
            
        return ans