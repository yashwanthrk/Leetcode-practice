# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # If both p and q are greater than root, move to the right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # If both p and q are smaller than root, move to the left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                # If one node is smaller and the other is larger, or one of the nodes is root,
                # then the current root is the LCA
                return root