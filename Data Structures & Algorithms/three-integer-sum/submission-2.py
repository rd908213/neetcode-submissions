class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # n log n
        solution = set()
        for i in range(len(nums)): # n
            virtual_list = nums[:i] + nums[i+1:]
            l = 0
            r = len(virtual_list) - 1
            while l < r: # log n
                if nums[i] + virtual_list[l] + virtual_list[r] < 0:
                    l += 1
                elif nums[i] + virtual_list[l] + virtual_list[r] > 0:
                    r -= 1
                else:
                    cor = [nums[i], virtual_list[l], virtual_list[r]] # Correct solution
                    cor.sort()
                    solution.add(tuple(cor))
                    l += 1
                    r -= 1
        
        return [list(tup) for tup in solution]