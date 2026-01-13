# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        track = {}

        def dfs(node, row, col):
            if not node:
                return
            
            if col in track:
                key = track[col]
                if row in key:
                    key[row].append(node.val)
                else:
                    key[row] = [node.val]
            else:
                track[col] = { row: [] }
                track[col][row].append(node.val)

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)

        res = []

        for col, rowtrack in sorted(track.items()):
            curr = []
            for row, values in sorted(rowtrack.items()):
                for value in sorted(values):
                    curr.append(value)
            res.append(curr)
            
        return res