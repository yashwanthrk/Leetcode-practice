class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, combo, start):
            if remain == 0:
                result.append(list(combo))
                return
            elif remain < 0:
                # Exceeded the scope, stop exploring further.
                return
            for i in range(start, len(candidates)):
                # Add the number into the combination.
                combo.append(candidates[i])
                # Give the current number another chance, rather than moving on.
                backtrack(remain - candidates[i], combo, i)
                # Remove the number from the combination since we have explored all valid combinations with it.
                combo.pop()

        result = []
        backtrack(target, [], 0)
        return result


# full reference, do it again