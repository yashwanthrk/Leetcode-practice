# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        

        def go_deep(node, depth):
            
            if not node:
                return depth

             # Increment the depth for the current level
            depth += 1
            
            # Recursively go deeper into the left and right subtrees
            left_depth = go_deep(node.left, depth)
            right_depth = go_deep(node.right, depth)

            # Return the maximum depth between the left and right subtrees
            return max(left_depth, right_depth)

        
        return go_deep(root, 0)
        