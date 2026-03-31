class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        pm=-1
        for i in range(len(arr)-1,-1,-1):
            c=arr[i]
            arr[i]=pm
            pm=max(c,pm)
        return arr
        