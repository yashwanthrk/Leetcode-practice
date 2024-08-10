class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        strs.sort()

        # Compare characters between the first and last string
        first, last = strs[0], strs[-1]
        result = []

        for f, l in zip(first, last):
            if f == l:
                result.append(f)
            else:
                break

        return "".join(result)