# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, node, subNode):
            if not node and not subNode:
                return True
            
            if node and subNode and node.val == subNode.val:
                return (self.sameTree(node.left, subNode.left) and
                        self.sameTree(node.right, subNode.right))
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not root:
                return False
            
            if root.val == subRoot.val and self.sameTree(root, subRoot):
                return True
            
            return (self.isSubtree(root.left, subRoot) or 
                    self.isSubtree(root.right, subRoot))