# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxPathSum(self, root: Optional[TreeNode]) -> int:
    #     maxSum = -float("inf")

    #     def dfs(node):
    #         nonlocal maxSum
    #         if not node:
    #             return 0
            
    #         maxSum = max(maxSum, dfs(node.left) + node.val + dfs(node.right))
    #         return node.val + max(dfs(node.left), dfs(node.right))

    #     dfs(root)
    #     return maxSum
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float("inf")

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0

            # compute once
            left = max(dfs(node.left), 0)   # ignore negatives
            right = max(dfs(node.right), 0)

            # update max path sum using this node as root
            maxSum = max(maxSum, left + node.val + right)

            # return the best single path up
            return node.val + max(left, right)

        dfs(root)
        return maxSum

     