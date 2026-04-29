from collections import deque
from typing import List, Optional

# Định nghĩa cấu trúc của một nút trong cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Trường hợp cây trống
        if not root:
            return []
        
        result = []
        # Sử dụng deque (double-ended queue) để tối ưu hiệu năng pop(0) với O(1)
        queue = deque([root])
        
        while queue:
            # Số lượng nút ở tầng hiện tại
            level_size = len(queue)
            level_sum = 0
            
            # Duyệt qua tất cả các nút thuộc tầng này
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Thêm các con của nút hiện tại vào hàng đợi cho tầng sau
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Tính trung bình cộng của tầng và thêm vào kết quả
            # Kết quả sẽ là float mặc định trong Python 3
            result.append(level_sum / level_size)
            
        return result