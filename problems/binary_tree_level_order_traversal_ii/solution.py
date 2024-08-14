# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        from collections import deque
        queue = deque([root])
        
        result = []
        
        while queue:
            
            level_items = []
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                level_items.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            if level_items:    
                result.append(level_items)

        return result[::-1]
