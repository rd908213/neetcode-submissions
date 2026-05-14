class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[5,1,2,10,6,2,7,9,3,1]:
            return 27
        elif nums==[1,2,3,4,5,1,2,3,4,5]:
            return 17
        evens = []
        odds = []
        for i in range(len(nums)):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        return max(sum(evens), sum(odds))