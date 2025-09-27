# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pathSum = 0

        def dfs(node):
            nonlocal pathSum
            if not node:
                return
            
            dfs(node.right)
            node.val += pathSum
            pathSum = node.val
            dfs(node.left)
        
        dfs(root)
        return root

