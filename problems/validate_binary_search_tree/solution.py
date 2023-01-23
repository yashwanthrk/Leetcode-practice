# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # NeetCode code referring

        if not root:
            return False

        def valid(node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left): 
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("+inf"))


        # def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        #     if not root: 
        #         return True
        #     if root.val <= floor or root.val >= ceiling:
        #         return False
        #     # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
        #     return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)