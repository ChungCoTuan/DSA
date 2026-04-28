class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        left_h = get_height(root.left)
        right_h = get_height(root.right)
        
        if left_h == right_h:
            return (1 << left_h) + self.countNodes(root.right)
        else:
            return (1 << right_h) + self.countNodes(root.left)