class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res=[0]*n
        stack=[]
        for i in logs:
            temp=i.split(":")
            temp[0],temp[2]=int(temp[0]),int(temp[2])
            if not stack:
                stack.append(temp)
            else:
                if temp[0]==stack[-1][0]:
                    if temp[1]=="start":
                        res[temp[0]]+=temp[2]-stack[-1][2]
                        stack.append(temp)
                    else:
                        res[temp[0]]+=temp[2]-stack[-1][2]+1
                        
                        stack.pop()
                        if stack:
                            stack[-1][2]=temp[2]+1
                        
                else:
                    res[stack[-1][0]]+=temp[2]-stack[-1][2]
                    stack.append(temp)
            
        return res
