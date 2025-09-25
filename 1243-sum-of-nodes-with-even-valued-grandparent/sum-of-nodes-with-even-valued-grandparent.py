# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = 0

        def sum_even_gp_child(node, parent, gparent):
            nonlocal total
            if not node:
                return 
            
            if gparent and gparent.val % 2 == 0:
                total += node.val
            
            sum_even_gp_child(node.left, node, parent)
            sum_even_gp_child(node.right, node, parent)
        
        sum_even_gp_child(root, None, None)
        return total
            
