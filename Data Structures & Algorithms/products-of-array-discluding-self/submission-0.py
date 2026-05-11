class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    product = product * nums[j]
            solution.append(product)
        return solution