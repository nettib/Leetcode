# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([[root, 0]])

        while q:
            qLen = len(q)
            prior = q[0][0]

            for i in range(qLen):
                node, level = q.popleft()

                if node.left:
                    q.append([node.left, level + 1])
                if node.right:
                    q.append([node.right, level - 1])
                
                if i == 0:
                    if level % 2 == 0:
                        if node.val % 2 == 0:
                            return False
                    else:
                        if node.val % 2 != 0:
                            return False
                else:
                    if level % 2 == 0:
                        if node.val % 2 == 0 or node.val <= prior.val:
                            return False
                    else:
                        if node.val % 2 != 0 or node.val >= prior.val:
                            return False
                    prior = node
            
        return True

                


