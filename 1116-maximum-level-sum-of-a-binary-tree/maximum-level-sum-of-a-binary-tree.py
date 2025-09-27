# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 1]])

        maxSum = -float("inf")
        smallestLevel = 1

        while q:
            trackSum = 0
            trackLevel = q[0][1]
            qLen = len(q)

            for _ in range(qLen):
                node, level = q.popleft()
                trackSum += node.val

                if node.left:
                    q.append([node.left, level + 1])
                if node.right:
                    q.append([node.right, level + 1])
            
            if trackSum > maxSum:
                smallestLevel = trackLevel
                maxSum = trackSum
        
        return smallestLevel