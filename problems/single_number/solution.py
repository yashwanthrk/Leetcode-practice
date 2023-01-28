class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         If we take XOR of zero and some bit, it will return that bit
# a⊕0=aa \oplus 0 = aa⊕0=a
# If we take XOR of two same bits, it will return 0
# a⊕a=0a \oplus a = 0a⊕a=0
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=ba \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# So we can XOR all bits together to find the unique number.
        a = 0
        for i in nums:
            a ^= i
        return a

