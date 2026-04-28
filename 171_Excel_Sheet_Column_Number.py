class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            # Chuyển ký tự thành số: 'A'->1, 'B'->2, ..., 'Z'->26
            # ord('A') là 65, nên ord(char) - 64 sẽ ra đúng thứ tự
            value = ord(char) - ord('A') + 1
            
            # Dịch chuyển các chữ số đã có sang trái (nhân 26) và cộng số mới
            result = result * 26 + value
            
        return result