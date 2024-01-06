class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:


        freq_count = defaultdict(list)
        for i, num in enumerate(nums):
            freq_count[num].append(i)
        
        max_frequency = max(len(indices) for indices in freq_count.values())
        
        if max_frequency == 1:
            return 1

        min_size = float('inf')

        for indices in freq_count.values():
            if len(indices) == max_frequency:
                min_size = min(min_size, indices[-1] - indices[0] + 1)

        return min_size
                


        