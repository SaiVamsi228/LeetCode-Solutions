from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.max_heap = []  # max heap (invert values)
        self.min_heap = []  # min heap

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)  # push to max_heap
        heappush(self.min_heap, -heappop(self.max_heap))  # balance: move largest of max_heap to min_heap

        # rebalance if min_heap gets bigger
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
