# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        new_k = [k]
        result = [None]  # To store the kth smallest element
#         In-Order Traversal:
# Visits nodes in ascending order in a Binary Search Tree.
# Counter Decrement:
# count keeps track of how many nodes have been visited. When count == 0, the current node is the kth smallest.
# Early Exit:
# Stops further recursion once the result is found.
        def depth(node):
            if not node:
                return
            
            depth(node.left)
            
            # Decrement k and check if the current node is the kth element
            new_k[0] -= 1
            if new_k[0] == 0:
                result[0] = node.val
                return
            
            depth(node.right)

        # Start the in-order traversal
        depth(root)
        return result[0]