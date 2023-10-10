class Solution:
    def searchRange(self, nums, target):
        
        # https://www.youtube.com/watch?v=6zhGS79oQ4k&ab_channel=takeUforward

        # Striver videos

        def lower_bound(nums, target):
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2

                # only difference
                if nums[mid] >= target: 
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        
        def upper_bound(nums, target):
                left, right = 0, len(nums) - 1
                ans = -1
                while left <= right:
                    mid = (left + right) // 2

                    # only difference
                    if nums[mid] > target: 
                        ans = mid - 1
                        right = mid - 1
                    else:
                        if nums[mid] == target:  # Update answer if the element is found
                            ans = mid
                        left = mid + 1

                return ans
        
        left = lower_bound(nums, target)
        right = upper_bound(nums, target)

        if left <= right:
            return [left, right]
        else:
            return [-1, -1]


