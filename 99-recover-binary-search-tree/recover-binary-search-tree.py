# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        fswap = None
        sswap = None
        prev = TreeNode(float("-inf"))

        def dfs(node):
            nonlocal fswap, sswap, prev
            if not node:
                return
            
            dfs(node.left)

            if prev.val > node.val:
                if not fswap:
                    fswap = prev
                sswap = node
            
            prev = node
            
            dfs(node.right)

        dfs(root)
        temp = fswap.val
        fswap.val = sswap.val
        sswap.val = temp
        