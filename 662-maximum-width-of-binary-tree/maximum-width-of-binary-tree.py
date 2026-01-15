# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxwidth = 0
        q = deque([[root, 1]])

        while q:
            first = q[0][-1]
            last = None
            for _ in range(len(q)):
                node, pos = q.popleft()
                last = pos
                if node.left:
                    q.append([node.left, 2 * pos])
                if node.right:
                    q.append([node.right, 2 * pos + 1])
            maxwidth = max(maxwidth, last - first + 1)
        
        return maxwidth