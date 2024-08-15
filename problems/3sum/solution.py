class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()  
        triplets = []
        
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1 

                else:
                    right -= 1  

        return triplets


        # h_index = {}
        # triplets = set()

        # for i, num in enumerate(nums):
        #     h_index[num] = i

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):

        #         # logic is nums[i] + nums[j] + desired_num = 0
        #         # make it ulta => desired_num = -nums[i] - nums[j]
        #         desired_num = - nums[i] - nums[j]
        #         if desired_num in h_index and h_index[desired_num] != i and  h_index[desired_num] != j:
        #             triplets.add(tuple(sorted([nums[i], nums[j], desired_num])))

        # return list(triplets)

        