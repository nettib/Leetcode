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
            track = []
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                track.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag:
                ans.append(track[::-1])
            else:
                ans.append(track)

            flag = 0 if flag else 1

        return ans
            


    