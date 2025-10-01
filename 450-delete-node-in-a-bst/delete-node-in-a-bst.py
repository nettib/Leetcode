# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # function to get the min value from the right subtree
    def getMinValue(self, node):
        curr = node

        while curr.left:
            curr = curr.left
        
        return curr
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = self.getMinValue(root.right)
                root.val = temp.val

                root.right = self.deleteNode(root.right, temp.val)
        
        return root


        