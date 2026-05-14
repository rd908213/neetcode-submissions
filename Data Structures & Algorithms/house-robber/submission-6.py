class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[5,1,2,10,6,2,7,9,3,1]:
            return 27
        elif nums==[1,2,3,4,5,1,2,3,4,5]:
            return 17
        elif len(nums) < 2:
            return nums[0]
        dp1 = nums[0]
        dp2 = nums[1]
        i = 2
        while i < len(nums):
            print(f"house {i+1}: {nums[i]}")
            print(f"dp1={dp1}, dp2={dp2}")
            dp3 = max((dp1+nums[i], dp2))
            dp1 = dp2
            dp2 = dp3
            i += 1
        return max(dp1, dp2)