# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # This will store the current count of nodes visited
        self.count = 0
        self.result = None
        
        def dfs(node):
            
            if not node or self.result is not None:
                return
            
            dfs(node.left)
            
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        
        return self.result