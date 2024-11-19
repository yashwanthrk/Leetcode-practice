class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # https://www.youtube.com/watch?v=EUDwWbvtB_Q&ab_channel=AlgoEngine

       # Build adjacency list and calculate in-degrees
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)  # prereq -> course
            in_degree[course] += 1

            # The adjacency list should represent the dependency direction, i.e., u -> v means you must complete v before u.
        
        # Initialize the queue with courses having no prerequisites
        
        queue = deque([])

        for i in range(numCourses): 
            if in_degree[i] == 0:
                queue.append(i)
        
        visited = 0
        result = []
        while queue:
            current_course = queue.popleft()
            result.append(current_course)
            
            visited += 1
            for neighbor in adj_list[current_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If you can process all numCourses nodes, it means the graph is a DAG (no cycles), and a topological order exists.
        # If all courses are visited, it means we can finish them
         # Step 5: Check for cycles
        if len(result) == numCourses:
            return result
        else:
            return []