class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[[]for i in range(len(nums)+1)]
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for ke,v in d.items():
            a[v].append(ke)
        res=[]
        for i in range(len(a)-1, 0 ,-1):
            for n in a[i]:
                res.append(n)
                if len(res)==k:
                    return res