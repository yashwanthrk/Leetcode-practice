class Solution:
      def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result_array = [0] * n
        left, right = 0, n - 1

        # very impo
        pos = n - 1


        while left <= right:

          left_sqr = nums[left] ** 2
          right_sqr = nums[right] ** 2

          if left_sqr > right_sqr:
            result_array[pos] = left_sqr
            left += 1
          else:
            result_array[pos] = right_sqr
            right -= 1
          
          pos -= 1

        return result_array
