
from collections import deque, defaultdict



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        graph_dict = defaultdict(list)
        for i, j in edges:
            graph_dict[i].append(j)
            graph_dict[j].append(i)

        
        # graph_dict = {}
        # for edge in edges:
        #     if edge[0] in graph_dict:
        #         graph_dict[edge[0]].add(edge[1])
        #     else:
        #         graph_dict[edge[0]] = {edge[1]}

        #     if edge[1] in graph_dict:
        #         graph_dict[edge[1]].add(edge[0])
        #     else:
        #         graph_dict[edge[1]] = {edge[0]}


        # if not source in graph_dict:
        #     return False

    #     visited = set()
    #     queue = deque([source])

    #     while queue:
    #         vertex = queue.popleft()
    # #         print(vertex)
            
    #         if vertex not in visited:
    #             print(visited)
    # #             print(vertex)  # or do something else with the vertex
    #             visited.add(vertex)
                
    #             #  graph[vertex] - visited performs a set difference operation. 
    # #             It subtracts the visited set from the set of adjacent vertices.        
    #             queue.extend(graph_dict[vertex] - visited)
    #             # print(queue)

    #     if source in visited and destination in visited:
    #         return True
        
    #     return False


        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            vertex = queue.popleft()

            if vertex == destination:
                return True



            for neighbor_node in graph_dict[vertex]:
                if neighbor_node not in visited:
                    visited.add(neighbor_node)
                    queue.append(neighbor_node)

        # return source in visited and destination in visited
        return False



        # if source == destination:
        #     return True

        # graph = defaultdict(list)
        # for i, j in edges:
        #     graph[i].append(j)
        #     graph[j].append(i)

        # queue = deque()
        # visited = set()

        # queue.append(source)
        # visited.add(source)

        # while queue:
        #     node = queue.popleft()
        #     if node == destination:
        #         return True

        #     for neighbor_node in graph[node]:
        #         if neighbor_node not in visited:
        #             queue.append(neighbor_node)
        #             visited.add(neighbor_node)
    
        # return False


            