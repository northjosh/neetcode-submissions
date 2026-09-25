class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return [x for x in range(len(nums) + 1) if x not in nums ][0]


        