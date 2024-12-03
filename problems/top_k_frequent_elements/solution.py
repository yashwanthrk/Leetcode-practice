class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        import heapq
        from collections import Counter

        min_heap = []

        num_counter = Counter(nums)

        for num, freq in num_counter.items():

            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for _, num in min_heap]

        