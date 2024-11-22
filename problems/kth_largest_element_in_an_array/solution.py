class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq

        heap = []

        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
#                 heapq.heappop() Works
# It removes the smallest element from the heap (the root of the binary heap).
# It rearranges the remaining elements to maintain the heap property:
# The new root will be the next smallest element.
# The heap remains a valid min-heap.
                # important step
                heapq.heappop(heap)

        return heap[0]