# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            
            if not node:
                return None

            # If node is either p or q, return the node itself
            if node == p or node == q:
                return node

            # If p and q are on different sides, the current node is the LCA
            if (p.val < node.val < q.val) or (q.val < node.val < p.val):
                return node

            # Traverse the left subtree if both p and q are smaller than node
            if p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q)

            # Traverse the right subtree if both p and q are greater than node
            if p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)

        return dfs(root, p, q)