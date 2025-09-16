# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(node, currMax):
            if not node:
                return 0
            
            if currMax <= node.val:
                res = 1
                currMax = node.val
            else:
                res = 0

            res += dfs(node.left, currMax)
            res += dfs(node.right, currMax)

            return res

        return dfs(root, root.val)