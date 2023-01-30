class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        # def calculate_sum(arr, sum):
        #     for num in arr:
        #         sum *= num
        #     return sum 
        # new_nums = [1] * len(nums)

        # for i in range(len(nums)):
        #     new_nums[i] = calculate_sum(nums[0:i], 1) * calculate_sum(nums[i+1:], 1)

        # return new_nums

        prefix_num =  [1] * len(nums)
        postfix_num  = [1] * len(nums)
        nums_3  = [1] * len(nums)



        prefix_num[0] = nums[0]
        postfix_num[-1] = nums[-1]

        for index in range(1, len(nums)):
            prefix_num[index] = prefix_num[index - 1] * nums[index]

        for index in range(len(nums) - 2, -1 , -1):
            postfix_num[index] = postfix_num[index + 1] * nums[index]
         
        # print(prefix_num, postfix_num)
        nums_3[0] =  postfix_num[1]
        nums_3[-1] = prefix_num[-2] 

        for i in range(1, len(nums) - 1):
            nums_3[i] = prefix_num[i - 1] * postfix_num[i+1]

        # print(nums_3)
        return nums_3

