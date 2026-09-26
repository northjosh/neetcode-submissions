class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0, n+1):
            s=0
            for i in range(32):
                if((num >> i) & 1):
                    s+=1
            res.append(s)
        return res
            


        