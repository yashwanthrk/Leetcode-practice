# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False

        def dfs(node, remaining_sum):

            if node is None:
                return False

            # Subtract the current node's value from the remaining sum
            remaining_sum -= node.val
            
            # Check if it's a leaf node and the remaining sum equals 0
            if node.left is None and node.right is None:
                return remaining_sum == 0

            
            # Recursively check the left and right subtrees

            return dfs(node.left, remaining_sum) or dfs(node.right, remaining_sum)

        return dfs(root, targetSum)

        
        
