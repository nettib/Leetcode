# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh = rh = 0
        l = r = root

        while l:
            lh += 1
            l = l.left
        
        while r:
            rh += 1
            r = r.right
        
        if lh == rh:
            return (1 << lh) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)