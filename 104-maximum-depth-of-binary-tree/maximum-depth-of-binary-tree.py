# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def dfs(node, count):
            nonlocal depth

            if not node:
                return
            
            depth = max(depth, count)
            dfs(node.left, count + 1)
            dfs(node.right, count + 1)
        
        dfs(root, 1)
        return depth 
