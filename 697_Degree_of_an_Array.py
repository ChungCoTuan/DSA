class Solution:
    def findShortestSubArray(self, nums):
        # Lưu vị trí đầu tiên xuất hiện của mỗi số
        first = {}
        # Lưu vị trí cuối cùng xuất hiện của mỗi số
        last = {}
        # Lưu tần suất xuất hiện
        count = {}
        
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
            count[x] = count.get(x, 0) + 1
            
        # Tìm độ của mảng (tần suất xuất hiện lớn nhất)
        degree = max(count.values())
        
        # Tìm độ dài ngắn nhất trong các ứng viên có tần suất bằng degree
        min_length = len(nums)
        for x in count:
            if count[x] == degree:
                # Độ dài mảng con chứa tất cả số x
                length = last[x] - first[x] + 1
                if length < min_length:
                    min_length = length
                    
        return min_length