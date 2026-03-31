class Solution:
    def confusingNumber(self, n: int) -> bool:
        d={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        res=""
        n=str(n)
        for i in n:
            c=d.get(i,"No")
            if c!="No":
                res+=d[i]

            else:
                return False
        res=res[::-1]
        print(n)
        return True if int(res)!=int(n) else False
        