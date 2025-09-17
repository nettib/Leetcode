# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([[root, 1]])

        while q:
            node1, level1 = q.popleft()
            if not q:
                res.append(node1.val)
            if q:
                node2, level2 = q[0]
                if level1 != level2:
                    res.append(node1.val)
            
            if node1.left:
                q.append([node1.left, level1 + 1])
            if node1.right:
                q.append([node1.right, level1 + 1])
        
        return res




