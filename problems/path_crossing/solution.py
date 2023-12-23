class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        N = [0, 1]
        E = [1, 0]
        S = [0, -1]
        W = [-1, 0]

        start_origin = [0, 0]

        visited = set()
        visited.add((0, 0))

        for ch in path:
            if ch == "N":
                start_origin[1] += N[1]
            elif ch == "E":
                start_origin[0] += E[0]
            elif ch == "S":
                start_origin[1] += S[1]
            else:
                start_origin[0] += W[0]


            # Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited.
            if tuple(start_origin) in visited:
                return True

            visited.add(tuple(start_origin))


        return False

        

