# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, node, subNode):
        if not node and not subNode:
            return True
        if not node or not subNode or node.val != subNode.val:
            return False
        return (self.isSameTree(node.left, subNode.left) and
                self.isSameTree(node.right, subNode.right))
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        