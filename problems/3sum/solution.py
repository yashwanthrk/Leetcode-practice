class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets_list = []


        for left in range(len(nums) - 2):

             # this step makes sure that we do not have any duplicates in our 
            #  result output
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]


                if total > 0:
                    right -= 1

                elif total < 0:
                    mid += 1


                else:
                    triplets_list.append([nums[left], nums[mid], nums[right]])


                    # Another conditional for not calculating duplicates

                    
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1


                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1

                    mid += 1
                    right -= 1

        return triplets_list
                        

