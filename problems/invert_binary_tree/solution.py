# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        

        def inverse(node):

            if not node:
                return

            node.left, node.right = node.right, node.left
            
            inverse(node.left)
            inverse(node.right)


        inverse(root)

        return root