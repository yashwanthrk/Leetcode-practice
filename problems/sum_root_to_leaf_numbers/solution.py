# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        total_path = []

        def dfs(node, root_to_leaf_path):
            if not node:
                return

            root_to_leaf_path.append(node.val)

            if not node.left and not node.right:
                string_result = ''.join(str(num) for num in list(root_to_leaf_path))
                total_path.append(string_result)
                root_to_leaf_path.pop()
                return

            
            dfs(node.left, root_to_leaf_path)
            dfs(node.right, root_to_leaf_path)
            
            root_to_leaf_path.pop()

        dfs(root, [])
        return sum(int(num)for num in total_path)