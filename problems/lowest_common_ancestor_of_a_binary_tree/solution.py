# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
           
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q) 
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in left and right subtrees of the current node, return the current node
        if left and right:
            return root
        
        # Otherwise, return the non-null node
        return left if left else right