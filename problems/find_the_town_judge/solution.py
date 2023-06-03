class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

       
        #  he should not follow anyone; 
        #  everyone should follow him

        arr = [[0, 0] for _ in range(n+1)]

        for t in trust:
            arr[t[0]][0] += 1
            arr[t[1]][1] += 1

        for i in range(1, n+1):
            if arr[i][0] == 0 and arr[i][1] == n-1:
                return i

        return -1