class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Helper function to check if Koko can finish eating all piles at speed k in h hours
        def k_hours(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            return hours <= h


        l = 1
        r = max(piles)

        # for k in range(l, r + 1):
        #     if k_hours(k):
        #         return k

        while l < r:
            k = (l + r) // 2
            if k_hours(k):
                r = k
            else:
                l = k + 1

        return r
