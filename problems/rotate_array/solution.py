class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        length = len(nums)
        k = k % length
        
        if not k or not nums:
            return

        nums[:] = nums[-k:] + nums[:length-k]
        
        
        # nums[-k:] = reversed(nums[-k:])
        # print(nums)
        # nums.reverse()

        # def reverse(start, end): 
        #     while start < end: 
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start += 1
        #         end -= 1 
                
        # num_len = len(nums)
        # k = k % num_len # if k > n, no point of total k rotations
        
        # reverse(0,num_len-1)
        # # reverse only till k elements
        # reverse(0, k - 1)
        # # now reverse remaining elements after k
        # reverse(k, num_len - 1) 




