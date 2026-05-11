class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            solution[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)):
            solution[-i - 1] *= postfix
            postfix *= nums[-i - 1]
        
        return solution
