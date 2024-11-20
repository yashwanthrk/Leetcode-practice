# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        


        #  queue = deque([(p, q)])
        
        #     while queue:
        #         node1, node2 = queue.popleft()
                
        #         if not node1 and not node2:
        #             continue
                
        #         if not node1 or not node2 or node1.val != node2.val:
        #             return False
                
        #         queue.append((node1.left, node2.left))
        #         queue.append((node1.right, node2.right))
            
        #     return True

        
        def are_same(p, q):
            
            if not p and not q:
                return True

            # if not p:
            #     return False
            
            # if not q:
            #     return False

            if not p or not q:
                return False

            if p.val != q.val:
                return False

        

            return are_same(p.left, q.left) and are_same(p.right, q.right)

        
        return are_same(p, q)