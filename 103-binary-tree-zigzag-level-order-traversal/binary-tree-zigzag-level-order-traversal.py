# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        flag = 0
        ans = []

        while q:
            level = []
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if flag:
                ans.append(level[::-1])
                flag -= 1
            else:
                ans.append(level)
                flag += 1
        
        return ans


