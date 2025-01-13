class StockSpanner:

    def __init__(self):

        self.nums = []
        
        self.st = []

        self.count = 0

    def next(self, price: int) -> int:
        
        if not self.st:

            self.st.append(self.count)

            self.count += 1

            self.nums.append(price)

            return 1
        
        elif self.st and self.nums[self.st[-1]] > price:

            self.nums.append(price)

            consec_days = self.count - self.st[-1]

            self.st.append(self.count)

            self.count += 1

            return consec_days
        
        elif self.st and self.nums[self.st[-1]] <= price:

            while self.st and self.nums[self.st[-1]] <= price:

                self.st.pop()

            if self.st :

                consec_days = self.count - self.st[-1]
            
            else:

                consec_days = self.count - (-1)
            
            self.st.append(self.count)

            self.nums.append(price)

            self.count += 1

            return consec_days




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)