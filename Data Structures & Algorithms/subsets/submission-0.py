class Solution:
    def subsets(self, nums: List[int], inProc = list()) -> List[List[int]]:
        solution = []
        if nums:
            for i in self.subsets(nums[1:], inProc):
                solution.append(i)
            for j in self.subsets(nums[1:], inProc + [nums[0]]):
                solution.append(j)
            print(solution)
            return solution
        else:
            return [inProc]