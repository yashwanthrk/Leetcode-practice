# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = {}

        def add_edge(node1, node2):
            if node1 in graph:
                graph[node1].append(node2)
            else:
                graph[node1] = [node2]

            if node2 in graph:
                graph[node2].append(node1)
            else:
                graph[node2] = [node1]

        def dfs(node):
            if not node:
                return
            if node.left:
                add_edge(node.val, node.left.val)
                dfs(node.left)
            if node.right:
                add_edge(node.val, node.right.val)
                dfs(node.right)

        dfs(root)
        
        if not graph.get(start, []):
            return 0

        def find_max_distance(graph, start):
            visited = set()
            distances = {node: float('inf') for node in graph}

            queue = deque([(start, 0)])
            visited.add(start)
            distances[start] = 0

            while queue:
                current_node, current_distance = queue.popleft()

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        distances[neighbor] = current_distance + 1
                        queue.append((neighbor, current_distance + 1))

            max_distance = max(distances.values())
            return max_distance

        return find_max_distance(graph, start)
        