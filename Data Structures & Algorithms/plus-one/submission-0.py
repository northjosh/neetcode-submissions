class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join(str(d) for d in digits))
        digits = int(digits)
        digits+=1
        return [int(x) for x in str(digits)]

        