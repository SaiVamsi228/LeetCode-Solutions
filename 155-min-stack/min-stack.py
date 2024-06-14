class MinStack:

    def __init__(self):
        
        self.stack = []

    def push(self, val: int) -> None:

        if not self.stack:

            self.stack.append([val,val])

            return 
        
        prevMin = self.peek()[1]

        if val < prevMin:

            self.stack.append([val,val])

        else:

            self.stack.append([val,prevMin])    
        

    def pop(self) -> None:
        
        if not self.stack:

            return 2**31 

        
        topEle = self.stack.pop()

        poppedEle = topEle[0]

        return poppedEle


    def top(self) -> int:
        
        return self.peek()[0]

    def getMin(self) -> int:

        return self.peek()[1]

    def peek(self):

        return self.stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()