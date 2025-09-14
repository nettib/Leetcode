# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, parent, grandParent):
            nonlocal total
            if not node:
                return
            if grandParent and grandParent.val % 2 == 0:
                total += node.val
            grandParent = parent
            parent = node
            dfs(node.left, parent, grandParent)
            dfs(node.right, parent, grandParent)
        dfs(root, None, None)
        return total