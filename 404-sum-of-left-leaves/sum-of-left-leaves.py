# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        q = deque([[root, None]])

        while q:
            node, mark = q.popleft()

            if mark == "l" and not node.left and not node.right:
                total += node.val
            
            if node.left:
                q.append([node.left, "l"])
            if node.right:
                q.append([node.right, "r"])
        
        return total