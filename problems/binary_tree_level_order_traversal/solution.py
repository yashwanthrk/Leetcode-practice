# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        # bfs ==> queue

        from collections import deque

        queue = deque([root])

        levels = []
        
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


            levels.append(curr_level)

        return levels         


        # while queue is not empty:
        #     initialize curr_level as an empty list
        #     determine size of current level as len(queue)

        #     for i in range(size of current level):
        #         pop a node from queue
        #         add node value to curr_level
        #         if left child exists, append to queue
        #         if right child exists, append to queue

        #     append curr_level to levels

        # return levels   
