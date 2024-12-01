# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        if not root:
            return False
        

        def has_sum(node, curr_sum):
            

            if not node:
                return False


            if not node.left and not node.right:
                return targetSum == curr_sum + node.val

            
            return has_sum(node.left, curr_sum + node.val) or has_sum(node.right, node.val + curr_sum)

        return has_sum(root, 0)
