# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     # Getting the minimum value from the BST
    def getMinValBst(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        #delete a node in BST
        if not root:
            return None
        
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
                print(root.val)
                node = self.getMinValBst(root.right)
                root.val = node.val
                print(node.val)
                root.right = self.deleteNode(root.right, node.val)
        return root
	

        