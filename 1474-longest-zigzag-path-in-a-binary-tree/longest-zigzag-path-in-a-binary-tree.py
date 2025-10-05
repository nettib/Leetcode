# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxPath = float("-inf")

        def dfs(node, count, gpm, pm):
            nonlocal maxPath
            if not node:
                return

            if not pm:
                count = 0
            elif gpm == pm:
                count = 1
            else:
                count += 1
            
            maxPath = max(maxPath, count)

            dfs(node.left, count, pm, "l")
            dfs(node.right, count, pm, "r")
        
        dfs(root, -1, None, None)
        return maxPath