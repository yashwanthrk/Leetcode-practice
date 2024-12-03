class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        max_heap = []

        for num in arr:
            distance = abs(num - x)
            # Push (-distance, -num) to ensure correct ordering
#             0.
#             Why Including -num Matters

# Heap Comparisons: The heap compares tuples element-wise. If the first elements are equal (i.e., distances are equal), it compares the second elements.
# Tie-Breaking Rule: According to the problem, when distances are equal, we prefer the smaller number (a < b).
# Including -num: By pushing -num, we invert the ordering of numbers. In the heap, this makes larger numbers appear "smaller" because -num for a larger num is more negativ
            heapq.heappush(max_heap, (-distance, -num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract the numbers from the heap
        result = [-num for _, num in max_heap]
        result.sort()
        return result