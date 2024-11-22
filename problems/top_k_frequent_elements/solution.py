class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        from collections import Counter
        import heapq

        num_freq = Counter(nums)
        heap = []
        for num, freq in num_freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))

        return [num for freq, num in heap]
