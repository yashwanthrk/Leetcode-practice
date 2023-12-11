class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
       
        length = len(nums)
        
        # Arrays to store left and right products
        L, R, answer = [0]*length, [0]*length, [0]*length

        # L[i] contains the product of all the elements to the left of i
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all the elements to the right of i
        R[length - 1] = 1
        for i in range(length - 2, -1, -1):
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            answer[i] = L[i] * R[i]

        return answer