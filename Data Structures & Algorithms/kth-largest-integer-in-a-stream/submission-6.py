import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums) # Make this a min-heap        
        self.nums, self.k = nums, k
        while len(self.nums) > k:
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0] # Returns kth largest
