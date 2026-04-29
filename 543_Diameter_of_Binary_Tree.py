class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            # cập nhật đường kính tại node này
            self.diameter = max(self.diameter, left + right)
            
            return max(left, right) + 1
        
        height(root)
        return self.diameter