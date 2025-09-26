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

        maxWidth = 0

        q = deque([[root, 1]])
        while q:
            fp = q[0][1]
            lp = q[-1][1]
            maxWidth = max(maxWidth, lp - fp + 1)

            qLen = len(q)
            for _ in range(qLen):
                node, index = q.popleft()

                if node.left:
                    q.append([node.left, 2 * index])
                if node.right:
                    q.append([node.right, 2 * index + 1])
        
        return maxWidth
