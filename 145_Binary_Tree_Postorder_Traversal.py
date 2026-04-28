# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, node, res):
        if not node:
            return
        
        # Thứ tự: Left -> Right -> Root
        self.helper(node.left, res)
        self.helper(node.right, res)
        res.append(node.val)