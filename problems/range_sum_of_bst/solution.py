# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:



        def dfs(node, result):

            if not node:
                return result

            result = dfs(node.left, result)
            if  node.val >= low and node.val <= high:
                result += (node.val)
            result = dfs(node.right, result)

            return result


        
        return dfs(root, 0)


        