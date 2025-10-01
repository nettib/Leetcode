# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        deepSum = 0

        while q:
            trackSum = 0
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()

                trackSum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            deepSum = trackSum
        
        return deepSum
