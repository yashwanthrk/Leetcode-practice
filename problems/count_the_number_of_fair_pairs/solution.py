class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
         
        nums.sort()  
        count = 0
        n = len(nums)

        for i in range(n):
            left = i + 1
            right = n - 1

            # Find the first index where nums[i] + nums[left] >= lower
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] >= lower:
                    right = mid - 1
                else:
                    left = mid + 1
            start = left

            # Find the last index where nums[i] + nums[right] <= upper
            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] <= upper:
                    left = mid + 1
                else:
                    right = mid - 1
            end = right

            # Add valid pairs count
            if start <= end:
                count += (end - start + 1)

        return count