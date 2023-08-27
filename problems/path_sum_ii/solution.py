# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        total_paths = []

        def dfs(node, current_sum, path):
            if not node:
                return
            
            current_sum += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if current_sum == targetSum:
                    total_paths.append(path[:])  # Make a copy of the path
                    
            else:
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)

            path.pop()  # Remove the last element from path before backtracking
        
        dfs(root, 0, [])
        return total_paths
