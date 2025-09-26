# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node, subNode):
            if not node and not subNode:
                return True
            
            if node and subNode and node.val == subNode.val:
                return (sameTree(node.left, subNode.left) and
                        sameTree(node.right, subNode.right))
            else:
                return False
        

        def check(node, subNode):
            if not node:
                return False
            
            if node.val == subNode.val:
                if sameTree(node, subNode):
                    return sameTree(node, subNode)
            
            return (check(node.left, subNode) or 
                    check(node.right, subNode))
        
        return check(root, subRoot)