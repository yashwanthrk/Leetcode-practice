# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # check isMirror cond
        #  i.e -> left.right and right.left are same
        #  same as right.left and left.right are same
        
 
        if not root:
            return False
        
        def check_mirror(left, right):
            if not left and not right :
                return True

            if left and right and left.val == right.val:
                return check_mirror(left.left, right.right) and check_mirror(left.right, right.left)

            return False

        return check_mirror(root.left, root.right)

        
                

            


            



        