class Solution:
    def hammingWeight(self, n: int) -> int:
        s=0

        for i in range(32):
            if((n >> i) & 1) ==1:
                s+=1
        return s
        