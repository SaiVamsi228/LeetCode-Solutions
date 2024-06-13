from queue import Queue
class MyStack:

    def __init__(self):
        
        self.queue = Queue()

        self.size = 0

    def push(self, x: int) -> None:

        s = self.size
        
        self.queue.put(x)

        for i in range(s):

            self.queue.put(self.queue.get())

        self.size += 1

    def pop(self) -> int:

        poppedEle = self.queue.get()

        self.size -= 1

        return poppedEle
        

    def top(self) -> int:

        if self.size:
            
            topEle = self.queue.get()

            self.size -= 1

            self.push(topEle)

            return topEle

    def empty(self) -> bool:

        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()