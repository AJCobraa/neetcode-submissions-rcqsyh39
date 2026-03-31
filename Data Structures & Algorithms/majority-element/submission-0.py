class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m,c=0,0
        for i in nums:
            if c==0:
                m=i
            c+=(1 if m==i else -1)
        return m
        