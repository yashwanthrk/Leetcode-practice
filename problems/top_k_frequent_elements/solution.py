class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencies = {}
        
        for element in nums:
            frequencies[element] = frequencies.get(element, 0) + 1
        
        # Sort elements based on their frequencies in descending order
        sorted_elements = sorted(frequencies, key=lambda x: frequencies[x], reverse=True)
        
        # Select the top k frequent elements
        print(sorted_elements)

        top_k_elements = sorted_elements[:k]
        return top_k_elements
