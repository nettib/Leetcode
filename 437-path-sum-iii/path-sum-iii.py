# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathCount = 0
        trackSum = { 0: 1 }

        def dfs(node, total):
            nonlocal pathCount
            if not node:
                return
            
            total += node.val

            if (total - targetSum) in trackSum:
                pathCount += trackSum[(total - targetSum)]
            
            trackSum[total] = trackSum.get(total, 0) + 1
            
            dfs(node.left, total)
            dfs(node.right, total)
            trackSum[total] -= 1

        dfs(root, 0)
        return pathCount
