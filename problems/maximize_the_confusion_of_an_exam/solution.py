class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
         
        count = {}  
        result = 0      
        left = 0      

        for right, char in enumerate(answerKey):
            count[char] = count.get(char, 0) + 1  
          
            # print((right - left + 1) , max(count.values()) , k )
            while (right - left + 1) - max(count.values()) > k:
                count[answerKey[left]] -= 1  # Shrink the window by moving the left pointer.
                left += 1

            result = max(result, right - left + 1)  

        return result