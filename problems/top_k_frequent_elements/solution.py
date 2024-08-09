class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Count frequencies of each element
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Bucket sort based on frequency
        freq = [[] for _ in range(len(nums) + 1)]
        for num, frequency in count.items():
            freq[frequency].append(num)
        
        # Gather top k frequent elements
        result = []
        for i in range(len(freq) - 1, 0, -1):
            # for i in range(len(freq) - 1, 0, -1): The loop starts from the highest possible frequency (len(nums) since freq has len(nums) + 1 elements) and decrements down to 1. 
            # This order ensures that the elements with the highest frequencies are considered first. 
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result