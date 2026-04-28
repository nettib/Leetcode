# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = [[root.val]]

        while q:
            n = len(q)
            temp = []

            for _ in range(n):
                node = q.popleft()
                if node.left:
                    temp.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    temp.append(node.right.val)
                    q.append(node.right)
            if len(temp) > 0:
                ans.append(temp[:])
            
        return ans 
                

            