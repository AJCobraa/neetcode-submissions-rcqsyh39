class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        post=1
        res=[]
        r=len(nums)-1
        while r>=0:
            res.append(post)
            post*=nums[r]
            r-=1
        res=res[::-1]
        for i in range(len(nums)):
            res[i]*=pre
            pre*=nums[i]
        return res