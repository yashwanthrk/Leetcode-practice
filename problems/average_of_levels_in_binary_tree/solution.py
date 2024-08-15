# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
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
                level_avg = sum(level_items) / len(level_items)
                result.append(level_avg)
        
        return result