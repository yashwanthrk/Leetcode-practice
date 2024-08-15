class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits

        # if the last digit is 9, it iterates from the last digit to the first, checking each digit. 
        for i in range(len(digits) - 1, -1, -1):
            
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0

        # If all digits are 9, we need an additional leading 1
        return [1] + digits