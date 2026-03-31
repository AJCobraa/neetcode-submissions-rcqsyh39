class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a={}
        for i in nums:
            a[i]=a.get(i,0)
        return len(a)!=len(nums)