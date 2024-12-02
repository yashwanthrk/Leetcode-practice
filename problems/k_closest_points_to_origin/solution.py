class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        if k == 0 or not points: 
            return []
        
        heap = []
    
        for x, y in points:
            dist = -(x**2 + y**2)  # Negate distance for max-heap behavior
            heapq.heappush(heap, (dist, (x, y)))  # Push current point into heap
            
            if len(heap) > k:  # If heap exceeds size k
                heapq.heappop(heap)  # Remove the farthest point
        
        return [point for _, point in heap]