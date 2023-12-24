class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        

        unique_path = set()


        for path in paths:
            unique_path.add(path[0])

        # Return the destination city, that is, the city without any path outgoing to another city.

        for path in paths:
            if path[1] not in unique_path:
                return path[1]
                
                

        