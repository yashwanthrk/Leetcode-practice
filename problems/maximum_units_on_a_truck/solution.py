class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort the array with 2nd element in descending order [[5,10],[2,5],[4,7],[3,9]]
        boxTypes.sort(key = lambda arr:arr[1], reverse = True)
        result = 0
        for numBoxes, units in boxTypes:
            if truckSize <= numBoxes:
                result += truckSize * units
                break
            result += numBoxes * units
            truckSize -= numBoxes
        
        
        
        return result

        
                