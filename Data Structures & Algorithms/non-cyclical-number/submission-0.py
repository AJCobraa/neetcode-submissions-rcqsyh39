class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.findSqSum(n)
        while slow!=fast:
            fast=self.findSqSum(fast)
            fast=self.findSqSum(fast)
            slow=self.findSqSum(slow)
        return True if slow==1 else False


    def findSqSum(self,n):
        s=0
        while n:
            s+=(n%10)**2
            n=n//10
        print(s)
        return s