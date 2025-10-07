# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        dead = set(to_delete)
        res = []
        
        def dfs(node):
            if not node:
                return
            
            if node.val in dead:
                if node.left and node.left.val not in dead:
                    res.append(node.left)
                if node.right and node.right.val not in dead:
                    res.append(node.right)

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in dead:
                return None
            return node
        
        if dfs(root):
            res.append(dfs(root))
        return res
            
