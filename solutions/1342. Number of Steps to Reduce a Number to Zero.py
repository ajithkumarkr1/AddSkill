class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        while num:
            if(num%2!=0):
                c+=1
                num=num-1
                continue
            num=num>>1
            c+=1
        return c
