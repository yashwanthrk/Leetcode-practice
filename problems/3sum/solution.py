class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        triplets_list = []

        def two_pointer_sum(current_value, low_ptr, high_ptr):

            while low_ptr < high_ptr:
                three_sum = current_value + nums[low_ptr] + nums[high_ptr]
                if three_sum > 0:
                    high_ptr -= 1
                elif three_sum < 0:
                    low_ptr  +=  1
                else:
                    triplets_list.append([current_value, nums[low_ptr], nums
[high_ptr]])
                    low_ptr += 1
                    while nums[low_ptr] == nums[low_ptr - 1] and low_ptr < high_ptr:
                        low_ptr += 1

            return

        nums = sorted(nums)

        for i in range(len(nums) - 2):            
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            two_pointer_sum(nums[i], i+1, len(nums) -1)
            
        return triplets_list





        