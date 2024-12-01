# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])  # 
        levels = []  
        
        odd_level = 0

        while queue:

            curr_level = []
            size = len(queue)  

            for i in range(size): 
                node = queue.popleft()
                curr_level.append(node.val) 
                if node.left:
                    queue.append(node.left)  
                if node.right:
                    queue.append(node.right)  


            if odd_level % 2 == 1:
                levels.append(curr_level[::-1])
            else:
                levels.append(curr_level) 
            
            odd_level += 1


        return levels
