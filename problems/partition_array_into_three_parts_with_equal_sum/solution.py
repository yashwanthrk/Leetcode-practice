class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        total = sum(arr)

        if total % 3 != 0:
            return False

        right_most = 0
        ideal = total // 3
        partition = 0
        for i, num in enumerate(arr):
            right_most += num

            if right_most == ideal:
                partition += 1

                # start from next partition
                right_most = 0

            if partition == 3:
                return True
            
        return False

            
