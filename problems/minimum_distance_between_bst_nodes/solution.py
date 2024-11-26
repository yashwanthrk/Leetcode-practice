# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        prev = [None]  
        min_diff = [float("inf")]

        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Process the current node
            if prev[0] is not None:  # Ensure prev is not None (skip for the first node)
                min_diff[0] = min(min_diff[0], abs(node.val - prev[0]))
            prev[0] = node.val 
            
            inorder(node.right)
        
        inorder(root)
        
        return min_diff[0]