class Solution:
    def countBits(self, n: int) -> List[int]:
        def decimalToBinary(num):
            binary_value =  bin(num).replace("0b", "")
            # print(int(binary_value))
            return len(binary_value.replace("0", ""))

        counting_bits_list = [decimalToBinary(num) for num in range(n+1)]
        
        return counting_bits_list        
