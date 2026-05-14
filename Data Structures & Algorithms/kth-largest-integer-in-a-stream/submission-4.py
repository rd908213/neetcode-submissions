import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums) # Make this a min-heap        
        self.nums, self.k = nums, k
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while self.k != len(self.nums):
            heapq.heappop(self.nums) # pop until only k nums left
        return self.nums[0] # Returns kth largest
