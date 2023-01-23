# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])


        center = len(nums) // 2
        
        root =  TreeNode(nums[center])
        
        left_sub_tree = nums[0:center]
        root.left = self.sortedArrayToBST(left_sub_tree)
        
       
        right_sub_tree = nums[center+1:]
        root.right = self.sortedArrayToBST(right_sub_tree)
        
        
        return root


