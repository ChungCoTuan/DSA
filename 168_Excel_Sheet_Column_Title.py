class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = []
        
        while columnNumber > 0:
            # 1. Trừ 1 để đưa về hệ 0-25
            columnNumber -= 1
            
            # 2. Lấy phần dư để tìm ký tự hiện tại (từ phải sang trái)
            remainder = columnNumber % 26
            char = chr(remainder + ord('A'))
            res.append(char)
            
            # 3. Chia cho 26 để xử lý hàng tiếp theo
            columnNumber /= 26
            
        # 4. Vì ta tìm từ hàng đơn vị ngược lên, nên cần đảo chuỗi
        return "".join(res[::-1])