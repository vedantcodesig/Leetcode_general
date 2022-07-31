class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod=1
        for i in range(len(nums)):
            prod=prod*nums[i]
        if prod>1:
            return 1
        elif prod==0:
            return 0
        else:
            return -1
        