# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count_node(node, count):
            if not node:
                return count

            return 1 + count_node(node.left, count) + count_node(node.right, count)

        return count_node(root, 0)