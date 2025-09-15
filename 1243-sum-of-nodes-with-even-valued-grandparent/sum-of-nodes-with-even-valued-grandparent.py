# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, parent, gparent):
            if not node:
                return 0

            currSum = node.val if gparent and gparent.val % 2 == 0 else 0

            leftSum = dfs(node.left, node, parent)
            rightSum = dfs(node.right, node, parent)

            return currSum + leftSum + rightSum
        
        return dfs(root, None, None)
