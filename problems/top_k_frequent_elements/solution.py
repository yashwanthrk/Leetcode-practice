from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}  

        for element in nums:
            frequencies[element] = frequencies.get(element, 0) + 1

        # Sort the elements based on their frequencies in descending order
        sorted_elements = sorted(frequencies, key=frequencies.get, reverse=True)
        
        # Select the top k frequent elements
        top_k_elements = sorted_elements[:k]

        return top_k_elements
       


        
        


                
                
                