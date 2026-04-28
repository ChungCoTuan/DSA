class Solution:
    def binaryTreePaths(self, root):
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            # nếu là lá
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            
            # đi tiếp
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")
        
        dfs(root, "")
        return res