class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        s1=sorted(nums)
        s2=max(s1)
        s1.pop(len(s1)-1)
        s3=max(s1)
        return (s2-1)*(s3-1)
        