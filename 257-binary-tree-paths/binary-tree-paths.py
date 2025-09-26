# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []

        def dfs(node):
            if not node:
                return
            
            path.append(node.val)

            if not node.left and not node.right:
                res.append("->".join(map(str, path)))
            
            dfs(node.left)
            dfs(node.right)

            path.pop()
        
        dfs(root)
        return res

