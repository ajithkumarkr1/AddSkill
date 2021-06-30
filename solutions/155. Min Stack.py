import sys
class MinStack:
​
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.top1=-1
        
​
    def push(self, val: int) -> None:
        if self.top1==-1:
            self.stack.append([val,val])
        else:
            if self.stack[self.top1][1]<val:
                self.stack.append([val,self.stack[self.top1][1]])
            else:
                self.stack.append([val,val])
        self.top1+=1
                
        
    def pop(self) -> None:
        self.top1-=1
        return self.stack.pop()
    
​
    def top(self) -> int:
        return self.stack[self.top1][0]
​
    def getMin(self) -> int:
        return self.stack[self.top1][1]
