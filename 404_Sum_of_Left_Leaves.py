class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        total = 0
        
        # kiểm tra con trái có phải leaf không
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        
        # tiếp tục duyệt
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        
        return total