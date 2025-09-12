# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        total = 0
        ans = False

        def dfs(node):
            nonlocal total
            nonlocal ans
            if node:
                total += node.val
                if not node.left and not node.right:
                    if total == targetSum:
                        if not ans:
                            ans = True
                        return

                dfs(node.left)
                if node.left:
                    total -= node.left.val
                dfs(node.right)
                if node.right:
                    total -= node.right.val
        
        dfs(root)
    
        return ans 


          
