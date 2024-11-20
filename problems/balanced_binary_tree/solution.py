# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        # https://www.youtube.com/watch?v=BrnZDIoScEA&list=PLKYEe2WisBTH48RzVCL_LQrGW-ahPY44S&index=3&ab_channel=GregHogg

        balanced = [True]

        def dfs(node):
            
            if not node:
                return 0


            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return False


            return 1 + (max(left_height, right_height))


        dfs(root)

        return balanced[0]