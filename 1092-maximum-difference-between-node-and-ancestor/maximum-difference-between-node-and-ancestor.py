# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = -float("inf")


        def dfs(node, maxAncestor, minAncestor):
            nonlocal maxDiff


            if not node:
                return
           
            maxDiff = max(maxDiff, abs(maxAncestor - node.val), abs(minAncestor - node.val))
            


            dfs(node.left, max(maxAncestor, node.val), min(minAncestor, node.val))
            dfs(node.right, max(maxAncestor, node.val), min(minAncestor, node.val))
       
        dfs(root, root.val, root.val)


        return maxDiff
