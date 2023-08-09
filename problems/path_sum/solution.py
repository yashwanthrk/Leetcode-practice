# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:
                return False
            
            current_sum += node.val
            if not node.left and not node.right:
                return current_sum == targetSum
            
            left_result = dfs(node.left, current_sum)
            if left_result:  # If the target sum is already found on the left path, no need to explore right
                return True
            
            return dfs(node.right, current_sum)

        return dfs(root, 0)
