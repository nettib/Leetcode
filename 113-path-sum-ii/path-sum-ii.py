# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(node, total, path):
            if not node:
                return
            
            total += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if total == targetSum:
                    ans.append(path.copy())

            dfs(node.left, total, path)
            dfs(node.right, total, path)
            path.pop()
        
        dfs(root, 0, [])
        
        return ans
            

'''
[5]
[5, 4]
[5, 4, 11]
[5, 4, 11, 7, 2, 8]
[5, 4, 11, 7, 2, 8, 13, 4]
'''     