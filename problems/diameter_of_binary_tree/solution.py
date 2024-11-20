# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        largest_diameter = [0]

        def height(node):
            
            if not node:
                return 0


            left_height = height(node.left)
            right_height = height(node.right)


            diameter = left_height + right_height

            largest_diameter[0] = max(largest_diameter[0], diameter)

            #  lets call recursively height on the root
            return 1 + max(left_height, right_height)


        height(root)

        return largest_diameter[0]