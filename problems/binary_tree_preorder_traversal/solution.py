# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        
        # Root -> Left --> Right


        # if not root:
        #     return []

        # result = []
        # stack = [root]

        # while stack:
        #     node = stack.pop()
        #     if node:
        #         result.append(node.val)
        #         # Push right child first, so that left child is processed before right.
        #         stack.append(node.right)
        #         stack.append(node.left)
                
        # return result

        traversal = []
        
        def dfs(node, traversal):
            
            if not node:
                return traversal

            traversal.append(node.val)
            
            if node.left:
                dfs(node.left, traversal)
            if node.right:
                dfs(node.right, traversal)



        dfs(root, traversal)



        return traversal
        