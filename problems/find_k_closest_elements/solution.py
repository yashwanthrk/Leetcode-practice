class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        abs_list = [abs(n - x) for n in arr]
        
        abs_sum = sum(abs_list[:k])
        min_sum = abs_sum
        
        # min index
        min_i = 0
        
        for i in range(1, len(arr) - k + 1):

            # absoulte sum like sliding window
            abs_sum = abs_sum - abs_list[i - 1] + abs_list[i + k - 1]
            
            # to keep the minimum index
            if abs_sum < min_sum:
                min_sum = abs_sum
                min_i = i
        
        return arr[min_i: min_i + k] 
