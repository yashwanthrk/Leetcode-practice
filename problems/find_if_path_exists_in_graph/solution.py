class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        #  dfs with recursion
        if source == destination:
            return True

        adj_list = collections.defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen = set()
        seen.add(source)

        # def dfs(i):
        #     if i == destination:
        #         return True

        #     for node in adj_list[i]:
        #         if node not in seen:
        #             seen.add(node)
        #             # soon the valid point is found
        #             if dfs(node):
        #                 return True
            
        #     return False

        # return dfs(source)



        # Iterative DFS:

            # For large graphs, recursion depth could exceed Python's limit. Consider using an iterative approach with a stack to avoid stack overflow issues.
            # Pseudo Code for Iterative DFS:

            # text
            # Copy code
            # - Initialize a stack with the `source` node.
            # - While the stack is not empty:
            #     - Pop the top node.
            #     - If the node is the destination, return True.
            #     - For each neighbor of the node:
            #         - If it’s not in the seen set:
            #             - Add it to the stack and mark it as visited.
            # - Return False if no path is found.

        
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            for neighbour_node in adj_list[node]:
                if neighbour_node not in seen:
                    seen.add(neighbour_node)
                    stack.append(neighbour_node)


        return False


    
