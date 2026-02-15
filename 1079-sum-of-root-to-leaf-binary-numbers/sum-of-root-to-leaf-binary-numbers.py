# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        def get_sum(node, curr):
            nonlocal total
            if not node:
                return
            
            curr.append(str(node.val))

            if not node.left and not node.right:
                total += int("".join(curr), 2)
            
            get_sum(node.left, curr)
            get_sum(node.right, curr)
            curr.pop()

        
        get_sum(root, [])

        return total