# https://leetcode.com/problems/find-median-from-data-stream

import heapq
class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if len(self.left_heap) == 0:
            self.left_heap.append(-num)
        elif num <= (-self.left_heap[0]):
            heapq.heappush(self.left_heap, -num)
            if len(self.left_heap) > (1 + len(self.right_heap)):
                top_left = -heapq.heappop(self.left_heap)
                heapq.heappush(self.right_heap, top_left)
        else:
            heapq.heappush(self.right_heap, num)
            if len(self.right_heap) > len(self.left_heap):
                top_right = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, -top_right)

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (((-1)*self.left_heap[0])+self.right_heap[0]) / 2
        else:
            return (-1)*self.left_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()