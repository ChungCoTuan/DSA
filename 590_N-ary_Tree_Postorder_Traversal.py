class Solution:
    def postorder(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            
            for child in node.children:
                dfs(child)
            
            res.append(node.val)
        
        dfs(root)
        return res