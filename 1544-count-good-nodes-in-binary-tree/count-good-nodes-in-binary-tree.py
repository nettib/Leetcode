# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodnodes = 0

        def get_good_nodes(node, curr_max):
            nonlocal goodnodes
            if not node:
                return
            
            if node.val >= curr_max:
                goodnodes += 1
            
            get_good_nodes(node.left, max(curr_max, node.val))
            get_good_nodes(node.right, max(curr_max, node.val))
        
        get_good_nodes(root, float("-inf"))
        return goodnodes
