# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(node, l, r):
            if not node:
                return True
            
            if node.val <= l.val or node.val >= r.val:
                return False
            
            
            return (checkBST(node.left, l, node) and 
                    checkBST(node.right, node, r))
        
        return checkBST(root, TreeNode(float("-inf")), TreeNode(float("inf")))