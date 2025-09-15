# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0

        def dfs(node, path, total):
            nonlocal res
            if not node:
                return 
            
            path.append(node.val)
            total += node.val
            if targetSum == total:
                res += 1
            currSum = total

            for i in range(len(path) - 1):
                currSum -= path[i]
                if currSum == targetSum:
                    res += 1
            
            dfs(node.left, path, total)
            dfs(node.right, path, total)

            path.pop()
        
        dfs(root, [], 0)

        return res
