class Solution:
    def findMode(self, root):
        from collections import defaultdict
        
        freq = defaultdict(int)
        
        def dfs(node):
            if not node:
                return
            
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        max_freq = max(freq.values())
        
        return [k for k, v in freq.items() if v == max_freq]