class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        
        if not self.st:

            self.st.append((val,val))
        
        else:

            prev_min = self.st[-1][1]

            cur_min = min(val,prev_min)

            self.st.append((val,cur_min))

    def pop(self) -> None:
        
        if self.st:

            return self.st.pop()[0]

    def top(self) -> int:
        
        if self.st:

            return self.st[-1][0]

    def getMin(self) -> int:

        if self.st:
            
            return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()