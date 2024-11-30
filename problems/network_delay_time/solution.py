class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        from collections import defaultdict
        from heapq import heappop, heappush

        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap to process nodes by shortest time
        heap = [(0, k)]  # (time_to_reach, node)
        visited = {}

        while heap:
            t, u = heappop(heap)
            # If the node is already visited, skip
            if u in visited:
                continue

            # Mark the node as visited with its shortest time
            visited[u] = t

            # If all nodes are visited, we can stop early
            if len(visited) == n:
                break

            # Push neighbors into the heap
            for v, w in graph[u]:
                if v not in visited:
                    heappush(heap, (t + w, v))

        # Check if all nodes are reachable
        return max(visited.values()) if len(visited) == n else -1
