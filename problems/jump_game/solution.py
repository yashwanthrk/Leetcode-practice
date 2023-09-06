class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  
        for i in range(len(nums)):
            print(i, max_reach)
            if i > max_reach:
                return False  #
            max_reach = max(max_reach, i + nums[i])  # Update max_reach based on current jump
            print(max_reach)
        return True  # If the last index can be reached

        