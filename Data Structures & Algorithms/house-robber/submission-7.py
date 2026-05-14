class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dp1 = nums[0]
        dp2 = max(nums[1], nums[0])
        i = 2
        while i < len(nums):
            print(f"house {i+1}: {nums[i]}")
            print(f"dp1={dp1}, dp2={dp2}")
            dp3 = max((dp1+nums[i], dp2))
            dp1 = dp2
            dp2 = dp3
            i += 1
        return max(dp1, dp2)