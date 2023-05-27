class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

    #     current_max_avg = (sum(nums[:k]) / k)

    #     for i in range(1, len(nums) - k + 1):
    #         current_max_avg = max(current_max_avg, (sum(nums[i:i+k]) / k))

    #     return current_max_avg


        window_sum = sum(nums[:k])
        current_max_avg = window_sum / k

        for i in range(1, len(nums) - k + 1):
            window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
            current_max_avg = max(current_max_avg, window_sum / k)

        return current_max_avg

