class Solution:
    def toLowerCase(self, s):
        res = ""
        for char in s:
            # Lấy mã ASCII của ký tự
            val = ord(char)
            # Các chữ cái in hoa 'A'-'Z' có mã từ 65 đến 90
            # Các chữ cái in thường 'a'-'z' có mã từ 97 đến 122
            # Độ lệch giữa hoa và thường là 32
            if 65 <= val <= 90:
                res += chr(val + 32)
            else:
                res += char
        return res