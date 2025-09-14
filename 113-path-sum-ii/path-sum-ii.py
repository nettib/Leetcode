# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        res = []

        def dfs(node, currSum):
            if not node:
                return 
            currSum += node.val
            path.append(node.val)
            if not node.left and not node.right and currSum == targetSum:
                res.append(path.copy())
            
            dfs(node.left, currSum)
            dfs(node.right, currSum)

            path.pop()

        dfs(root, 0)

        return res