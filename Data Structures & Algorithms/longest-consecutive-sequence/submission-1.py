class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() # Time complexity = n log n
        print(nums)
        longest = 0 # Longest Seq
        current = 0 # Current Seq
        for i in range(len(nums)): # Will prbably have to rewrite thiss loop
            if nums[i] == nums[i-1] + 1 or current == 0:
                current += 1
                print(nums[i])
            elif nums[i] == nums[i-1]:
                continue
            else:
                longest = max(current, longest)
                print(f"longest: {longest}")
                current = 1
        return max(current, longest)
                