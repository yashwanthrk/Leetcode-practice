# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        def calculate_sum(node, current_sum):
            
            if not node:
                return False

            current_sum += node.val

            # Check if it's a leaf node and if the sum matches the targetSum
            if not node.left and not node.right:
                return current_sum == targetSum

            # Recursively check the left and right subtrees
            left_path = calculate_sum(node.left, current_sum)
            print(current_sum)
            right_path = calculate_sum(node.right, current_sum)

            return left_path or right_path

        return calculate_sum(root, 0)