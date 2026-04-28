class Solution:
    def invertTree(self, root):
        if not root:
            return None
        
        # đổi trái phải
        root.left, root.right = root.right, root.left
        
        # đệ quy xuống dưới
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root