import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        cnt = 0
        for i in nums:
            heapq.heappush(hq , i)
            cnt +=1
            if cnt > k:
                heapq.heappop(hq)
                cnt-=1
        return hq[0]

# Kth largest element in stream
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hq = []
        self.cnt = 0
        self.k = k
        for i in nums:
            heapq.heappush(self.hq , i)
            self.cnt +=1
            if self.cnt > self.k:
                heapq.heappop(self.hq)
                self.cnt-=1

    def add(self, val: int) -> int:
        heapq.heappush(self.hq , val)
        self.cnt +=1
        if self.cnt > self.k:
            heapq.heappop(self.hq)
            self.cnt-=1
        return self.hq[0]
