# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
 # Handle the edge case where the tree is empty
        if not root:
            return []

        queue = deque([root])  # Initialize the queue with the root node
        levels = []  # To store the result

        while queue:
            curr_level = []
            size = len(queue)  # Number of nodes at the current level

            for i in range(size):  # Process all nodes at the current level
                node = queue.popleft()
                curr_level.append(node.val)  # Add the node's value to the current level
                if node.left:
                    queue.append(node.left)  # Add left child to the queue
                if node.right:
                    queue.append(node.right)  # Add right child to the queue

            levels.append(curr_level)  # Append the current level to the result

        return levels