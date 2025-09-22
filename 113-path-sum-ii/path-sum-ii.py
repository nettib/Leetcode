# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        track = []
        
        def dfs(node, pathsum):
            if not node:
                track.append(None)
                return
            
            pathsum += node.val
            track.append(node.val)

            if not node.left and not node.right and pathsum == targetSum:
                res.append(track.copy())
            
            dfs(node.left, pathsum)
            track.pop()
            dfs(node.right, pathsum)
            track.pop()
	
        dfs(root, 0)
        return res

# 5 [5]
# 4 [5, 4]
# 11 [5, 4, 11]
# 7 [5, 4, 11, 7]
# 2 [5, 4, 11, 2]
# 8 [5, 8]
# 13 [5, 8, 13]
# 4 [5, 8, 4]
# 5 [5, 8, 4, 5]
# 1 [5, 8, 4, 1]  