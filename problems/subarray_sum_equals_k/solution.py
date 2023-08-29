class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0

        # base case
        # single prefix sum
        prefix_sum = {0: 1}

        current_sum = 0
        for num in nums:
            current_sum += num
            diff = current_sum - k

            count += prefix_sum.get(diff, 0)

            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)
            

        return count



        # https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode
        # watch video multiple times