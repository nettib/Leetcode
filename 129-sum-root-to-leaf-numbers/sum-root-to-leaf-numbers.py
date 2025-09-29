# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        allPathSum = 0

        def dfs(node, track):
            nonlocal allPathSum
            if not node:
                return
            
            track += str(node.val)
            if not node.left and not node.right:
                allPathSum += int(track)

            dfs(node.left, track)
            dfs(node.right, track)
        
        dfs(root, "")
        return allPathSum