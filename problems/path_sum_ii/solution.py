# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        
        result = []

        if root is None:
            return []

        def dfs(node, remaining_sum, current_path):
            
            if node is None:
                return
            
            current_path.append(node.val)
            
            remaining_sum -= node.val
            
            # Check if we are at a leaf node and if the remaining sum equals 0
            if node.left is None and node.right is None and remaining_sum == 0:
                # Add a copy of the current path to the result
                result.append(list(current_path))  
            
            dfs(node.left, remaining_sum, current_path)
            dfs(node.right, remaining_sum, current_path)
            
            # Backtrack by removing the last node from the path
            current_path.pop()
        
        dfs(root, targetSum, [])
        
        return result
        
        
