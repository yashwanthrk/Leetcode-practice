class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        n = len(arr)
        count = 1

        for i in range(1, n):

            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 1

            if count > n // 4:
                return arr[i - 1]

        # Handle the case where the last element is the special element
        if count > n // 4:
            return arr[n - 1]

        # If no element found
        return -1