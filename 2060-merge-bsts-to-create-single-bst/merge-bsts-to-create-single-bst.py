# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        def isValid(node, l, r):
            if not node:
                return True
            
            if node.val <= l or node.val >= r:
                return False
            
            return (isValid(node.left, l, node.val) and 
                    isValid(node.right, node.val, r))
        root_map = {}

        leafs = set()

        for tree in trees:
            root_map[tree.val] = tree
            if tree.left:
                leafs.add(tree.left.val)
            if tree.right:
                leafs.add(tree.right.val)
        
        root = None
        for tree in trees:
            if tree.val not in leafs:
                if root:
                    return None
                root = tree

        if not root:
            return None

        used = {root.val}

        def merge(node):
            if not node:
                return
            if node.val in root_map and node.val not in used:
                used.add(node.val)
                tree = root_map[node.val]
                node.left = tree.left
                node.right = tree.right
            
            merge(node.left)
            merge(node.right)
    
        merge(root)

        if len(used) != len(trees):
            return None
        
        if not isValid(root, float("-inf"), float("inf")):
            return None
        
        return root