# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([[root, None, None]])
        total = 0

        while q:
            node = q.popleft()

            if node[2] and node[2].val % 2 == 0:
                total += node[0].val
            
            if node[0].left:
                q.append([node[0].left, node[0], node[1]])
            if node[0].right:
                q.append([node[0].right, node[0], node[1]])
        
        return total

