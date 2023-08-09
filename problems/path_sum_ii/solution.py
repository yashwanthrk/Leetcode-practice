# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        total_list = []

        def dfs(node, current_sum, current_list):
            if not node:
                return
            
            current_list.append(node.val)
            current_sum += node.val

            if not node.left and not node.right:
                if current_sum == targetSum:
                    # list is mutuable, be careful
                    total_list.append(list(current_list))  # Append a copy of current_list

                # important step - pop the last element, when either of the leaf nodes are reached
                current_list.pop()  # Remove the last element from current_list
                return
            
            dfs(node.left, current_sum, current_list)
            dfs(node.right, current_sum, current_list)
            current_list.pop()  # Remove the last element from current_list after exploring both left and right

        dfs(root, 0, [])
        return total_list