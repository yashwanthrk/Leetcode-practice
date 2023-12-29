# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


        def isMirror(left, right):
            # Base case: if both nodes are None, they are symmetric
            if not left and not right:
                return True

            # If one of the nodes is None and the other is not, they are not symmetric
            if not left or not right:
                return False

            # Check if the values of the nodes are equal and if the subtrees are mirrors
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        # Check if the tree is symmetric starting from the root
        return isMirror(root, root)