class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq
        
        # Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Iterate over the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:  # Compare with the smallest in the heap
                heapq.heappop(min_heap)  # Remove the smallest
                heapq.heappush(min_heap, num)  # Add the current number

        return min_heap[0]  # The root of the heap is the kth largest element