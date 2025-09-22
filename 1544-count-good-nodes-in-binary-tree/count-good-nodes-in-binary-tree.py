# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goods = 0

        def dfs(node, currMax):
            nonlocal goods
            if not node:
                return
            
            if node.val >= currMax:
                goods += 1
            
            dfs(node.left, max(currMax, node.val))
            dfs(node.right, max(currMax, node.val))
        
        dfs(root, root.val)
        return goods